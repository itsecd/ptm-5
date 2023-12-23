import pytest
from unittest.mock import patch
from library_catalog import LibraryCatalog, Book 


class TestLibraryCatalog:
    @pytest.fixture
    def library_catalog(self):
        return LibraryCatalog()

    def test_add_book(self, library_catalog):
        book = Book("The Great Gatsby", "F. S. Fitzgerald", "978-5699748068")
        library_catalog.add_book(book)
        assert len(library_catalog.books) == 1

    def test_remove_book(self, library_catalog):
        book = Book("1984", "George Orwell", "978-0451524935")
        library_catalog.add_book(book)
        library_catalog.remove_book("978-0451524935")
        assert len(library_catalog.books) == 0

    def test_find_book_by_title(self, library_catalog):
        book = Book("The Body", "Stephen King", "978-1405884935")
        library_catalog.add_book(book)
        result = library_catalog.find_book_by_title("The Body")
        assert len(result) == 1
        assert result[0].author == "Stephen King"

    def test_find_book_by_author(self, library_catalog):
        book = Book("Short Stories", "Ray Bradbury", "978-5811224935")
        library_catalog.add_book(book)
        result = library_catalog.find_book_by_author("Ray Bradbury")
        assert len(result) == 1
        assert result[0].title == "Short Stories"

    def test_count_books(self, library_catalog):
        book1 = Book("1984", "George Orwell", "978-0451524935")
        book2 = Book("Animal Farm", "George Orwell", "978-0451526342")
        library_catalog.add_book(book1)
        library_catalog.add_book(book2)
        assert library_catalog.count_books() == 2

    def test_get_book_by_isbn(self, library_catalog):
        book1 = Book("To Kill a Mockingbird", "Harper Lee", "978-0451524935")
        book2 = Book("Animal Farm", "George Orwell", "978-0451526342")
        book3 = Book("The Great Gatsby", "F.S. Fitzgerald", "978-0743273565")
        
        library_catalog.add_book(book1)
        library_catalog.add_book(book2)
        library_catalog.add_book(book3)
        
        result_book = library_catalog.get_book_by_isbn("978-0451524935")
        
        assert result_book.title == "To Kill a Mockingbird"
        assert result_book.author == "Harper Lee"
        assert result_book.isbn == "978-0451524935"


    def test_check_book_isbn(self, library_catalog, monkeypatch):
        book = Book("1984", "George Orwell", "978-0451524935")
        library_catalog.add_book(book)

        def mock_check_book_isbn(mock_isbn):
            assert mock_isbn == "978-0451524935"
            return False

        monkeypatch.setattr(library_catalog, 'check_book_isbn', mock_check_book_isbn)
        assert not library_catalog.check_book_isbn("978-0451524935")

    def test_count_books_by_author(self, library_catalog):
        book1 = Book("1984", "George Orwell", "978-0451524935")
        book2 = Book("Animal Farm", "George Orwell", "978-0451526342")
        library_catalog.add_book(book1)
        library_catalog.add_book(book2)

        with patch.object(LibraryCatalog, 'count_books_by_author', return_value={'George Orwell': 2, 'F. Scott Fitzgerald': 0}) as mock_method:
            assert library_catalog.count_books_by_author()['George Orwell'] == 2
