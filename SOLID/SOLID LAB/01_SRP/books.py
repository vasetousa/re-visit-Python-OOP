class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self, name):

        self.name = name
        self.books = []

    def add_book(self, book: Book):
        booklet = [b for b in self.books if b.title == book.title]
        if booklet:
            return f'We have this book in the library.'
        self.books.append(book)
        return f'Book {book.title} added to the library.'

    def remove(self, title):
        booklet = [b for b in self.books if b.title == title]
        if booklet:
            self.books.remove(booklet[0])
            return f'The {title} was removed from the library.'
        return f"We don't have {title} in the library"

    def find_book(self, title):
        booklet = [b for b in self.books if b.title == title]
        if booklet:
            booklet = booklet[0]
            return f'We found the "{title}" and it is located in our {booklet.location} library '
        return f"We don't have the '{title}' in the library"

    def __repr__(self):
        result = ''
        result += f'Library "{self.name}"\nBooks: \n'
        for x in self.books:
            result += f'- {x.title}, written by {x.author}\n'
        return result



book = Book("Blah", "Ivan", "Pernik")
book1 = Book("Kosh", "Gosho", "Sofia")
book2 = Book("Vampires", "Pesho", "Varna")
lib = Library("Grand Library")
print(book.turn_page(100))
lib.add_book(book)
lib.add_book(book1)
lib.add_book(book2)
print(lib.find_book("Kosh"))
print(lib.find_book("Prop"))
print(lib)
