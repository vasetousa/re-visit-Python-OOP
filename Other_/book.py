

class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

    def open_book_at_page(self, page:int):
        return f'The book was opened on page {page}'

book = Book("Shining", 'Steven King', 300)

print(f'The book "{book.name}", from {book.author}, has {book.pages} pages')
print(book.open_book_at_page(33))


class Car():
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} "{self.model}" with engine {self.engine}'


car = Car('Kia', 'Rio', '1.3L')
print(car.get_info())