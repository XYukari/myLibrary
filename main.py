import os

from Account import Admin, User, Login
from Book import Library

if __name__ == '__main__':
    login = Login()
    lib = Library()

    login.addAccount(Admin('Jack', '001', '19750101', lib))
    login.addAccount(User('Amy', '002', '20030201', lib))

    while True:
        account = login.getAccount()
        title = 'Admin' if isinstance(account, Admin) else 'User'
        print('Welcome, ' + title + ' ' + account.name)

        while True:
            cmd = input('Command: ')
            if cmd == 'exit':
                print()
                break
            if cmd == 'printList' or cmd == 'sortList':
                getattr(account, cmd)()
            else:
                title = input('Title: ')
                getattr(account, cmd)(title)

        os.system("cls")
