class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Can only add objects of type Book to the catalog.")
        self.books.append(book)

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return True
        return False

    def find_book_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]

    def find_book_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

    def list_all_books(self):
        return self.books

    def count_books(self):
        return len(self.books)

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def update_book(self, isbn, updated_book):
        for i, book in enumerate(self.books):
            if book.isbn == isbn:
                self.books[i] = updated_book
                return True
        return False
    
    def check_book_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return True
        return False

    def count_books_by_author(self):
        author_count = {}
        for book in self.books:
            if book.author in author_count:
                author_count[book.author] += 1
            else:
                author_count[book.author] = 1
        return author_count


if __name__ == "__main__":
    catalog = LibraryCatalog()

    book1 = Book("1984", "George Orwell", "978-0451524935")
    book2 = Book("Animal Farm", "George Orwell", "978-0451526342")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    print(catalog.check_book_isbn("978-0451524935"))

    print(catalog.count_books_by_author())

    catalog.remove_book("978-0451524935")
    print(catalog.check_book_isbn("978-0451524935"))
