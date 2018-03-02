"""
7.5 Online book Reader
Design the data structures for an online book reader system
"""

# Objects: page, book, reader, user

class Page:
    def __init__(self, text):
        self.__text = __text

    def getText(self):
        return self.__text

    # may want to add highlighting functionality

class Book:
    def __init__(self, pages, title, author):
        self.__pages = pages # list of __pages
        self.__currentPage = 0
        self.__title = title
        self.__author = author

    def nextPage(self):
        """Flip to next page & get page information. Returns -1 if at end."""
        # ensure not at end of book
        if self.__currentPage > len(self.__pages):
            return -1
        self.__currentPage += 1
        return self.__pages[self.getPageNum()]

    def prevPage(self):
        """Flip to previous page & get page information. Returns -1 if at begginning."""
        # ensure not before first page
        if self.__currentPage < 1:
            return -1
        self.__currentPage -= 1
        return self.__pages[self.getPageNum()]

    def getPageNum(self):
        """Returns page number, first page is 0."""
        return self.__currentPage

    def goToPage(self, num):
        self.__currentPage = 0

    def startOver(self):
        """Starts book over from begginning"""
        self.goToPage(0)

class Reader:
    def __init__(self, books):
        """Books is list of books"""
        self.__library = books
        self.__checkedOut = []

    def getAllBooks(self):
        return self.__library

    def getUnavailableBooks(self):
        return self.__checkedOut

    def getAvailableBooks(self):
        return self.getAllBooks not in self.getUnavailableBooks()

    def checkoutBook(self, book):
        # ensure not checkout out already
        if book in self.getUnavailableBooks():
            return -1
        # add book to checkedout Books
        self.__checkedOut.append(book)

    def returnBook(self, book):
        # set book to start from page 0 again
        book.startOver()
        return self.__checkedOut.pop(book)

class User:
    def __init__(self, name):
        self.__name = name
