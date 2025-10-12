class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_details(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def get_details(self):
        return f"{super().get_details()}, File Size: {self.file_size}KB"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def get_details(self):
        return f"{super().get_details()}, Page Count: {self.page_count}"
    
class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Book: {book.title} by {book.title}.")
        else:
            print("Invalid item. Please add a valid book object.")

    def list_books(self):
        if not self.books:
            print("The library is currently empty.")
            return
        
        print("---Library Books---")
        for book in self.books:
            print(book.get_details())