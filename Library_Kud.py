# from operator import attrgetter

# import self as self
import operator
from typing import Any


class People:

    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.readerList = []

    def getFullName(self):
        return " %s %s %s %d " % (self.name, self.surname, self.gender, self.age)

    def addBookToReaderList(self, book):  # добавить книгу в readerList
        self.readerList.append(book)  # список книг, которые на руках у читателя
        print("book is added to the readerlist")

    def deleteBookFromReaderList(self, book):
        self.readerList.remove(book)
        print("book is removed to the readerlist")

    def displayReaderList(self):  # вывести список  книг у читателей (в наличии)
        print("У читателя есть следующие книги:")
        for book in self.readerList:
            print(str(book))

    def __str__(self):
        # return "%d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing)
        return " %s %s %s %d " % (self.name, self.surname, self.gender, self.age)


class Book:
    # isInLib: bool = True

    def __init__(self, id, namebook, author, Publishing, yearPublishing):
        self.id = id
        self.namebook = namebook
        self.author = author
        self.Publishing = Publishing
        self.yearPublishing = yearPublishing
        self.isInLib = True

    def setBookInLib(self, x: bool):  # x - принимает True/False
        self.isInLib = x

    def getBookInLib(self):
        return self.isInLib

    def getFullNameBook(self):
        return "id= %d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing)

    def __str__(self):
        return "%d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing)

    def __repr__(self):
        return repr("%d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing))


class Library1:

    def __init__(self):
        self.readerList = []
        self.listBooks = []  # список книг
        self.listPeople = []  # список посетителей

    def add_Book(self, book):  # добавить книгу
        self.listBooks.append(book)

    def delete_Book(self, bookObj):  # удалить книгу
        for book in self.listBooks:
            if book == bookObj:
                self.listBooks.remove(bookObj)
            # continue
            else:
                print('Данной книги в библиотеке нет!')
        #  break

    def give_Book(self, peopleObj, bookObj):  # отдать книгу читателю
        for book in self.listBooks:
            if book == bookObj:
                peopleObj.addBookToReaderList(book)  # добавляем книгу  в список читателя
                book.setBookInLib(False)
                print("книга " + bookObj.namebook + " отдана читателю " + peopleObj.name + " " + peopleObj.surname)

    def accept_Book(self, peopleObj1, bookObj1):  # принять книгу  от читателя
        for book in peopleObj1.readerList:
            if book == bookObj1:
                peopleObj1.deleteBookFromReaderList(book)
                bookObj1.setBookInLib(True)
                print(
                    "книга " + bookObj1.namebook + " забрана у читателя " + peopleObj1.name + " " + peopleObj1.surname)

    def displayBibleBook(self):  # вывести список  всех книг в библиотеке
        print("Список всех книг: ")
        for book in self.listBooks:
            print(str(book))

    def displayNotInLibBook(self):  # вывести список книг  (не в наличии)
        print("Список книг не в наличии: ")
        for book in self.listBooks:
            # if book.getBookInLib() == False:
            if not book.getBookInLib():
                print(str(book))

    def displayAvailableBooks(self):  # вывести список книг   в наличии
        print("Список книг в наличии: ")
        for book in self.listBooks:
            # if book.getBookInLib() == True:
            if book.getBookInLib():
                print(str(book))

    def sortList(self, list_x, i):
        sorted(list_x, key=lambda t: t[i])
    # sorted(str(book), key=operator.itemgetter(i))


# def sort_Books(self, list_x):


#   print(sorted(list_x, key=lambda list: list.namebook))


people_1 = People('Igor', 'Kudrya', 'male', 46)
people_2 = People('Svitlana', 'Perley', 'female', 36)
print(people_1.getFullName(), '\n', people_2.getFullName())


book1 = Book(2234, "'Улісс',", "Дж.Джойс:", "Дніпро,", 1930)
book2 = Book(3234, "'Безсоння',", "С.Кінг:", "Вашингтон,", 1980)
book3 = Book(1234, "'Старий і море',", "Гемінгвей:", "Нью-Йорк,", 1923)
print(book1.getFullNameBook(), '\n', book2.getFullNameBook())

lib1 = Library1()
lib1.add_Book(book1)
lib1.add_Book(book2)
lib1.add_Book(book3)

lib1.give_Book(people_1, book3)
lib1.give_Book(people_2, book2)

lib1.displayBibleBook()
print("====================================")
lib1.displayNotInLibBook()
print("====================================")
lib1.displayAvailableBooks()

lib1.accept_Book(people_2, book2)

lib1.displayBibleBook()
print("====================================")
lib1.displayNotInLibBook()
print("====================================")
lib1.displayAvailableBooks()

# print(sorted(lib1.listBooks, key=lambda p: p[0]))
lib1.sortList(lib1.readerList, 0)  # не работает без сообщения об ошибке
lib1.displayBibleBook()  # не работает без сообщения об ошибке

# lib1.sortList(lib1.listBooks, 0)  # не работает  сообщением об ошибке
# lib1.displayBibleBook()
