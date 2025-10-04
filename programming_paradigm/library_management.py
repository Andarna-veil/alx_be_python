class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """Represents a library that holds a collection of books."""

    def __init__(self):
        self._books = []  # private list of Book instances

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Book '{title}' checked out successfully."
        return f"Book '{title}' is not available."

    def return_book(self, title):
        """Return a checked-out book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Book '{title}' returned successfully."
        return f"Book '{title}' was not checked out."

    def list_available_books(self):
        """Print the list of books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
