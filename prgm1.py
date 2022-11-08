class Book:
    def _init_(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.checkedOut = False
    def return_pages(self):
        print(self.pages)
        return self.pages

    def return_title(self):
        print(self.title)
        return self.title

class Library:
    def _init_(self):
        collection = {}

    def addExistingBook(self, book):
        collection[book.title] = book.author

    def addNewBook(self, title, author, pages): # create a book
        new_book = Book(title, author, pages)
        collection[title] = new_book.author # access the author
        if title in collection.keys():
            title.change_value_of_checkedOut()
        else:
            print("This book is not in the collection.")

def main():
    # if you are using Python 2.x, change input() to raw_input()
    title = str(input("Enter the title of the book. "))
    author = str(input("Enter the author of the book. "))
    pages = int(input("Enter the number of pages in the book. "))
    myBook = Book(title, author, pages)
    myLib = Library()
    myLib.addExistingBook(myBook)
   length = len(myBook)
   print(length)
   print (myBook)
   