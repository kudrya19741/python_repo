class People(dict):

    def __init__(self, name, surname, gender, age):
        dict.__init__(self)

        self['name'] = name
        self['surname'] = surname
        self['gender'] = gender
        self['age'] = age
        self.readerList = []  # список книг у читателей

    def getFullName(self):
        return " %s %s %s %d " % (self['name'], self['surname'], self['gender'], self['age'])

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
        return f'{self["name"]}, {self["surname"]}, {self["gender"]}, {self["age"]}'


class Book(dict):

    def __init__(self, id, namebook, author, Publishing, yearPublishing):
        dict.__init__(self)

        self['id'] = id  # ключи словаря
        self['namebook'] = namebook  # ключи словаря
        self['author'] = author  # ключи словаря
        self['Publishing'] = Publishing  # ключи словаря
        self['yearPublishing'] = yearPublishing  # ключи словаря
        self['isInLib'] = True

    def setBookInLib(self, x: bool):  # x - принимает True/False
        self['isInLib'] = x

    def getBookInLib(self):
        return self['isInLib']

    def getFullNameBook(self):
        return f'{self["id"]}, {self["namebook"]}, {self["author"]}, {self["Publishing"]}, {self["yearPublishing"]}'

    def __str__(self):
        return f'{self["id"]}, {self["namebook"]}, {self["author"]}, {self["Publishing"]}, {self["yearPublishing"]}'


class Library(dict):

    def __init__(self):
        dict.__init__(self)

        self["listBooks"] = []  # список книг
        self["listPeople"] = []  # список посетителей

    def add_Book(self, book):  # добавить книгу
        self["listBooks"].append(book)

    def delete_Book(self, bookObj):  # удалить книгу
        if bookObj in self["listBooks"]:
            self["listBooks"].remove(bookObj)
        else:
            print("Данной книги в библиотеке нет!")

    def give_Book(self, peopleObj, bookObj):  # отдать книгу читателю
        if bookObj in self["listBooks"]:
            peopleObj.addBookToReaderList(bookObj)  # добавляем книгу  в список читателя
            bookObj.setBookInLib(False)


    def accept_Book(self, peopleObj, bookObj):  # принять книгу  от читателя
        if bookObj in peopleObj.readerList:
            peopleObj.deleteBookFromReaderList(bookObj)
            bookObj.setBookInLib(True)


    def add_People(self, people):  # добавить читателя
        self["listPeople"].append(people)

    def displayBibleBook(self):  # вывести список  всех книг в библиотеке
        print("Список всех книг: ")
        for book in self["listBooks"]:
            print(str(book))


    def displayNotInLibBook(self):  # вывести список книг  (не в наличии)
        print("Список книг не в наличии: ")
        for book in self["listBooks"]:
            # if book.getBookInLib() == False:
            if not book.getBookInLib():
                print(str(book))

    def displayAvailableBooks(self):  # вывести список книг   в наличии
        print("Список книг в наличии: ")
        for book in self["listBooks"]:
            if book.getBookInLib():
                print(str(book))

    def sortList(self, key):  # Сортировка listBooks
        print(sorted(self["listBooks"], key=lambda t: t[key]))


lib = Library()

people_1 = People('Igor', 'Kudrya', 'male', 46)
people_2 = People('Svitlana', 'Perley', 'female', 36)

lib.add_People(people_1)
lib.add_People(people_2)

print(lib)
print("====================================")
book1 = Book(2234, 'Улісс', 'Дж.Джойс', 'Дніпро', 1930)
book2 = Book(3234, 'Безсоння', 'С.Кінг', 'Вашингтон', 1980)
book3 = Book(1234, 'Старий і море', 'Гемінгвей', 'Нью-Йорк', 1923)

lib.add_Book(book1)
lib.add_Book(book2)
lib.add_Book(book3)

print(lib)
print("====================================")
lib.displayBibleBook()
print("====================================")
lib.give_Book(people_1, book3)
lib.give_Book(people_1, book1)
lib.give_Book(people_2, book2)
people_1.displayReaderList()
people_2.displayReaderList()

lib.displayBibleBook()
print("====================================")
lib.displayNotInLibBook()
print("====================================")
lib.displayAvailableBooks()
print("====================================")
lib.accept_Book(people_2, book2)
print("====================================")
lib.displayBibleBook()
print("====================================")
lib.displayNotInLibBook()
print("====================================")
lib.displayAvailableBooks()
'''
id
namebook
author
Publishing
yearPublishing
'''
# lib = Library()
print("==================================== namebook")
lib.sortList('namebook')

print("==================================== yearPublishing")
lib.sortList("yearPublishing")
