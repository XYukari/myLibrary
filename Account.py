class Account:

    def __init__(self, name, id, pwd, library):
        self.name = name
        self.id = id
        self.pwd = pwd
        self.library = library

    def query(self, title):
        id = self.library.query(title)
        if id == -1:
            print('Book not found')
        elif id == 0:
            print('Book found but not available')
        else:
            print('Book is available')


class Admin(Account):

    def sortList(self):
        self.library.sortList()

    def addBook(self, title):
        self.library.addBook(title)

    def removeBook(self, title):
        self.library.removeBook(title)

    def printList(self):
        self.library.printList()


class User(Account):
    def borrowBook(self, title):
        self.library.borrowBook(title)

    def returnBook(self, title):
        self.library.returnBook(title)


class Login:
    def __init__(self):
        self.accountList = []

    def addAccount(self, account):
        self.accountList.append(account)

    def getAccount(self):
        id = input('Id: ')
        pwd = input('Password: ')
        for account in self.accountList:
            if account.id == id and account.pwd == pwd:
                return account
