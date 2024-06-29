class Book:
    def __init__(self, title):
        self.title = title
        self.isAvailable = 0


class Library:
    def __init__(self):
        self.bookList = []

    # 1 for available; 0 for unavailable; -1 for not found.
    def query(self, title):
        for book in self.bookList:
            if book.title == title:
                return book.isAvailable
        return -1

    def addBook(self, title):
        self.bookList.append(Book(title))
        print('You added book ' + title)

    def removeBook(self, title):
        self.bookList.remove(Book(title))
        print('You removed book ' + title)

    def sortList(self):
        self.bookList.sort(key=lambda book1, book2: book1.title.lower() < book2.title.lower())
        print('Books have been sorted by title')

    def printList(self):
        print('Book List:')
        for i, book in enumerate(self.bookList):
            print(str(i + 1) + '. ' + book.title)

    def borrowBook(self, title):
        for book in self.bookList:
            if book.title == title and book.isAvailable == 1:
                book.isAvailable = 0
                print('You borrowed book ' + title)
                break

    def returnBook(self, title):
        for book in self.bookList:
            if book.title == title and book.isAvailable == 0:
                book.isAvailable = 1
                print('You returned book ' + title)
                break
