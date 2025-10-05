class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = "Available"
    
    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = "Checked out"

    def return_book(self):
        """Mark the book as available"""
        self._is_checked_out = "Available"

    def is_available(self):
        """Return True is the book is available"""
        return self._is_checked_out == "Available"
    
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self._is_checked_out})"

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only instances of Book can be added to the library.")

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return "f'{book.title}' has been checked out"
            return "f'{self.title}' is either not available or does not exist."
    
    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                return "f'{book.title}' has been returned."
            return "f No checked out copy of '{title}' was found."
        
    def list_available_books(self):
        """List all available books in the library."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            return "No books are currently available."
        return "\n".join(str(book) for book in available)
    
# Create some book instances
book1 = Book("Atomic Habits", "James Clear")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("1984", "George Orwell")

# Create a library and add books
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# List available books
print(library.list_available_books())

# Check out a book
print(library.check_out_book("1984"))

# Try to check it out again
print(library.check_out_book("1984"))

# Return the book
print(library.return_book("1984"))

# List available books again
print(library.list_available_books())
