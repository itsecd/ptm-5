import logging
import pytest
from main import Library, Person, Book


@pytest.fixture
def library():
    """Aункция для создания экземпляра Library"""
    return Library()


def test_add_person(library):
    """Тест для метода add_person"""
    person = Person("John", 28)
    library.add_person(person)
    assert person in library.people


def test_remove_person(library):
    """Тест для метода remove_person"""
    person = Person("Jane", 35)
    library.add_person(person)
    library.remove_person(person)
    assert person not in library.people


def test_add_book(library):
    """Тест для метода add_book"""
    book = Book("The Catcher in the Rye", "J.D. Salinger")
    library.add_book(book)
    assert book in library.books


def test_remove_book(library):
    """Тест для метода remove_book"""
    book = Book("1984", "George Orwell")
    library.add_book(book)
    library.remove_book(book)
    assert book not in library.books


def test_lend_book(library):
    """Тест для метода lend_book"""
    person = Person("Charlie", 40)
    book = Book("Animal Farm", "George Orwell")
    library.add_person(person)
    library.add_book(book)
    library.lend_book(book, person)
    assert book.owner == person
    assert book in person.owned_books


@pytest.mark.parametrize("filename", ["test_inventory.txt", "nonexistent_file.txt"])
def test_save_to_txt(library: Library, filename: str) -> None:
    """Тест для метода save_to_txt"""
    person1 = Person("Item 1", 25)
    person2 = Person("Item 2", 30)
    library.add_person(person1)
    library.add_person(person2)
    library.save_to_txt(filename)


@pytest.mark.parametrize("filename", ["test_inventory.txt", "nonexistent_file.txt"])
def test_load_from_txt(library: Library, filename: str) -> None:
    """Тест для метода load_from_txt"""
    library.load_from_txt(filename)


def test_error_handling(library, caplog):
    """Тест обработки ошибок при добавлении/удалении"""
    with caplog.at_level(logging.WARNING):
        library.remove_person(Person("Nonexistent Person", 99))
        assert "Attempt to delete a non-existent person" in caplog.text
        library.remove_book(Book("Nonexistent Book", "Unknown Author"))
        assert "Attempt to delete a non-existent book" in caplog.text
        library.lend_book(Book("Nonexistent Book", "Unknown Author"), Person("Nonexistent Person", 99))
        assert "It is impossible to issue a book" in caplog.text