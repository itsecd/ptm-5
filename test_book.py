# импортируем модуль, который мы хотим протестировать
import book_manager

# импортируем pytest и mock для создания моков и стабов
import pytest
from unittest import mock

# создаем фикстуру, которая будет очищать список книг перед каждым тестом
@pytest.fixture(autouse=True)
def clear_books():
    book_manager.books.clear()

# создаем фикстуру, которая будет добавлять несколько книг в список для тестирования
@pytest.fixture
def sample_books():
    book_manager.add_book('Book1', 'Author1', 300, '2022-01-01', 20.0, 'Fiction')
    book_manager.add_book('Book2', 'Author2', 250, '2022-02-15', 15.0, 'Mystery')
    book_manager.add_book('Book3', 'Author3', 400, '2022-03-20', 35.0, 'Fantasy')

# тестируем функцию добавления книги
def test_add_book():
    # проверяем, что список книг пустой
    assert len(book_manager.books) == 0
    # добавляем книгу
    book_manager.add_book('Book4', 'Author4', 350, '2022-04-01', 18.0, 'Romance')
    # проверяем, что список книг содержит одну книгу
    assert len(book_manager.books) == 1
    # проверяем, что книга имеет правильные атрибуты
    book = book_manager.books[0]
    assert book['title'] == 'Book4'
    assert book['author'] == 'Author4'
    assert book['pages'] == 350
    assert book['release_date'] == '2022-04-01'
    assert book['cost'] == 18.0
    assert book['genre'] == 'Romance'

# тестируем функцию удаления книги
def test_remove_book(sample_books):
    # проверяем, что список книг содержит три книги
    assert len(book_manager.books) == 3
    # удаляем книгу
    book_manager.remove_book('Book2')
    # проверяем, что список книг содержит две книги
    assert len(book_manager.books) == 2
    # проверяем, что книга была удалена
    titles = [book['title'] for book in book_manager.books]
    assert 'Book2' not in titles

# тестируем функцию сортировки книг по новизне
def test_sort_by_release_date(sample_books):
    # сортируем книги по дате выпуска
    sorted_books = book_manager.sort_by_release_date()
    # проверяем, что книги отсортированы в правильном порядке
    assert sorted_books[0]['title'] == 'Book3'
    assert sorted_books[1]['title'] == 'Book2'
    assert sorted_books[2]['title'] == 'Book1'

# тестируем функцию сортировки книг по количеству страниц
def test_sort_by_pages(sample_books):
    # сортируем книги по количеству страниц
    sorted_books = book_manager.sort_by_pages()
    # проверяем, что книги отсортированы в правильном порядке
    assert sorted_books[0]['title'] == 'Book2'
    assert sorted_books[1]['title'] == 'Book1'
    assert sorted_books[2]['title'] == 'Book3'

# тестируем функцию группировки книг по жанрам
def test_group_by_genre(sample_books):
    # группируем книги по жанрам
    genres = book_manager.group_by_genre()
    # проверяем, что получили правильный словарь
    assert genres == {'Fiction': 1, 'Mystery': 1, 'Fantasy': 1}

# тестируем функцию расчета, сколько книг можно купить на заданную сумму
def test_count_books_affordable(sample_books):
    # проверяем, сколько книг можно купить на $30
    affordable_books = book_manager.count_books_affordable(30.0)
    # проверяем, что получили две книги
    assert len(affordable_books) == 2
    # проверяем, что это правильные книги
    titles = [book['title'] for book in affordable_books]
    assert 'Book1' in titles
    assert 'Book2' in titles

# тестируем функцию добавления книги с использованием параметризации
# для проверки разных входных данных
@pytest.mark.parametrize('title, author, pages, release_date, cost, genre', [
    ('Book5', 'Author5', 200, '2022-05-01', 10.0, 'Horror'),
    ('Book6', 'Author6', 450, '2022-06-01', 30.0, 'Sci-Fi'),
    ('Book7', 'Author7', 100, '2022-07-01', 5.0, 'Comedy')
])
def test_add_book_parametrized(title, author, pages, release_date, cost, genre):
    # проверяем, что список книг пустой
    assert len(book_manager.books) == 0
    # добавляем книгу с параметрами
    book_manager.add_book(title, author, pages, release_date, cost, genre)
    # проверяем, что список книг содержит одну книгу
    assert len(book_manager.books) == 1
    # проверяем, что книга имеет правильные атрибуты
    book = book_manager.books[0]
    assert book['title'] == title
    assert book['author'] == author
    assert book['pages'] == pages
    assert book['release_date'] == release_date
    assert book['cost'] == cost
    assert book['genre'] == genre

# тестируем функцию удаления книги с использованием мока
# для подмены глобальной переменной books
# Тест, который использует настоящий список книг вместо мока
def test_remove_book_real():
    # добавляем книгу в список книг
    book_manager.add_book('Book8', 'Author8', 500, '2022-08-01', 40.0, 'Thriller')
    # проверяем, что список книг содержит одну книгу
    assert len(book_manager.books) == 1
    # удаляем книгу
    book_manager.remove_book('Book8')
    # проверяем, что список книг пустой
    assert len(book_manager.books) == 0


