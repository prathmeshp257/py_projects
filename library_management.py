'''
Write a Library class with no_of_books and books as two instance variables.
Write a program to create a library from this Library class and show how you can print all books,
add a book and get the number of books using different methods.
Show that your program doesn't persist the books after the program is stopped!
'''

class library:
    books = []
    books_count = int(len(books))

    def __init__(self):
        print("Welcome to the Library Management Tool ")
        return

    def add_books(self, *args):
        for elem in args:
            self.books.append(elem)
            self.books_count += 1
        return

    def set_books_count(self, count):
        self.books_count = int(count)

    def audit_check(self):
        if self.books_count != len(self.books):
            print("Wrong Inventory")
        else:
            print("All Goes Well")

    def __str__(self):
        print("This is Library management Tool")




a = library()
a.add_books("India 2020", "RamKatha", "Shyam")
print(a.books)
# a.set_books_count(1)
print(a.books_count)
a.add_books("mahabharat")
print(a.books)
print(a.books_count)
a.set_books_count(1)
a.audit_check()

print(library.__dict__)
library()
