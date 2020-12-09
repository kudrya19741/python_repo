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
        return "%d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing)

    def __str__(self):
        return "%d %s %s %s %d" % (self.id, self.namebook, self.author, self.Publishing, self.yearPublishing)


class Library1(list):

    def give_Book(self, peopleObj, bookObj):  # отдать книгу читателю
        # if bookObj in self.listBooks:
        if bookObj in self:
            peopleObj.addBookToReaderList(bookObj)  # добавляем книгу  в список читателя
            bookObj.setBookInLib(False)
            print("Книга %s, отдана читателю %s %s" % (bookObj.namebook, peopleObj.surname, peopleObj.name))

    def accept_Book(self, peopleObj1, bookObj1):  # принять книгу  от читателя
        if bookObj1 in peopleObj1.readerList:
            peopleObj1.deleteBookFromReaderList(bookObj1)
            bookObj1.setBookInLib(True)
            print("Книга %s, получена от читателя %s %s" % (bookObj1.namebook, peopleObj1.surname, peopleObj1.name))

    def displayBibleBook(self):  # вывести список  всех книг в библиотеке
        print("Список всех книг: ")
        for book in self:
            print(str(book))

    def displayNotInLibBook(self):  # вывести список книг  (не в наличии)
        print("Список книг не в наличии: ")
        for book in self:
            # if book.getBookInLib() == False:
            if not book.getBookInLib():
                print(str(book))

    def displayAvailableBooks(self):  # вывести список книг   в наличии
        print("Список книг в наличии: ")
        for book in self:
            if book.getBookInLib():
                print(str(book))

    def sortList(self, key):  # Сортировка listBooks
        if key == 'namebook':
            self.sort(key=lambda t: t.namebook)
        elif key == 'yearPublishing':
            self.sort(key=lambda t: t.yearPublishing)
        else:
            print('Error! No key!')


people_1 = People('Igor', 'Kudrya', 'male', 46)
people_2 = People('Svitlana', 'Perley', 'female', 36)
print(people_1.getFullName(), '\n', people_2.getFullName())
print("====================================")
book1 = Book(2234, "'Улісс',", "Дж.Джойс:", "Дніпро,", 1930)
book2 = Book(3234, "'Безсоння',", "С.Кінг:", "Вашингтон,", 1980)
book3 = Book(1234, "'Старий і море',", "Гемінгвей:", "Нью-Йорк,", 1923)
print(book1.getFullNameBook(), '\n', book2.getFullNameBook())
print("====================================")
lib1 = Library1()
lib1.append(book1)
lib1.append(book2)
lib1.append(book3)

lib1.give_Book(people_1, book3)
lib1.give_Book(people_2, book2)

lib1.displayBibleBook()
print("====================================")
lib1.displayNotInLibBook()
print("====================================")
lib1.displayAvailableBooks()
print("====================================")
lib1.accept_Book(people_2, book2)
print("====================================")
lib1.displayBibleBook()
print("====================================")
lib1.displayNotInLibBook()
print("====================================")
lib1.displayAvailableBooks()

'''
id
namebook
author
Publishing
yearPublishing
'''
print("====================================")
lib1.sortList('namebook')
lib1.displayBibleBook()

print("====================================")
lib1.sortList('yearPublishing')
lib1.displayBibleBook()
