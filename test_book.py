import pytest
from datetime import date

# Это ваш код, который я импортирую для тестирования
import book_manager

# Это фикстура, которая создает список книг для тестирования
@pytest.fixture
def books():
    return [
        {
            'title': 'The Catcher in the Rye',
            'author': 'J.D. Salinger',
            'pages': 277,
            'release_date': date(1951, 7, 16),
            'cost': 10.99,
            'genre': 'Novel'
        },
        {
            'title': 'The Hitchhiker\'s Guide to the Galaxy',
            'author': 'Douglas Adams',
            'pages': 180,
            'release_date': date(1979, 10, 12),
            'cost': 5.99,
            'genre': 'Science Fiction'
        },
        {
            'title': 'The Lord of the Rings',
            'author': 'J.R.R. Tolkien',
            'pages': 1216,
            'release_date': date(1954, 7, 29),
            'cost': 19.99,
            'genre': 'Fantasy'
        }
    ]

# Это тест, который проверяет, что функция add_book добавляет книгу в список books
def test_add_book(books):
    # Это книга, которую я хочу добавить
    book = {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'pages': 223,
        'release_date': date(1997, 6, 26),
        'cost': 9.99,
        'genre': 'Fantasy'
    }
    # Это вызов функции add_book с книгой в качестве аргумента
    book_manager.add_book(book['title'], book['author'], book['pages'], book['release_date'], book['cost'], book['genre'])
    # Это утверждение, которое проверяет, что книга добавлена в список books
    assert book in book_manager.books

# Это тест, который проверяет, что функция remove_book удаляет книгу из списка books по названию
def test_remove_book(books):
    # Это название книги, которую я хочу удалить
    title = 'The Catcher in the Rye'
    # Это вызов функции remove_book с названием в качестве аргумента
    book_manager.remove_book(title)
    # Это утверждение, которое проверяет, что книга удалена из списка books
    assert title not in [book['title'] for book in book_manager.books]

# Это тест, который проверяет, что функция sort_by_release_date сортирует список books по дате выпуска в обратном порядке
def test_sort_by_release_date(books):
    # Это вызов функции sort_by_release_date
    sorted_books = book_manager.sort_by_release_date()
    # Это утверждение, которое проверяет, что список books отсортирован по дате выпуска в обратном порядке
    assert sorted_books == [books[2], books[1], books[0]]

# Это тест, который проверяет, что функция sort_by_pages сортирует список books по количеству страниц
def test_sort_by_pages(books):
    # Это вызов функции sort_by_pages
    sorted_books = book_manager.sort_by_pages()
    # Это утверждение, которое проверяет, что список books отсортирован по количеству страниц
    assert sorted_books == [books[1], books[0], books[2]]

# Это тест, который проверяет, что функция group_by_genre группирует список books по жанру и возвращает словарь с количеством книг в каждом жанре
def test_group_by_genre(books):
    # Это вызов функции group_by_genre
    genres = book_manager.group_by_genre()
    # Это утверждение, которое проверяет, что функция group_by_genre возвращает правильный словарь с жанрами и количеством книг
    assert genres == {'Novel': 1, 'Science Fiction': 1, 'Fantasy': 2}

# Это тест, который проверяет, что функция count_books_affordable возвращает список книг, которые стоят не больше заданной суммы
def test_count_books_affordable(books):
    # Это сумма, которую я хочу использовать для тестирования
    amount = 15.00
    # Это вызов функции count_books_affordable с суммой в качестве аргумента
    affordable_books = book_manager.count_books_affordable(amount)
    # Это утверждение, которое проверяет, что функция count_books_affordable возвращает правильный список книг
    assert affordable_books == [books[0], books[1]]

# Это параметризованный тест, который проверяет, что функция print_menu выводит правильное меню на экран
@pytest.mark.parametrize('choice, expected', [
    ('0', 'Goodbye!'),
    ('1', 'Enter book title: '),
    ('2', 'Enter the title of the book to remove: '),
    ('3', 'Books sorted by release date:'),
    ('4', 'Books sorted by pages:'),
    ('5', 'Books grouped by genre:'),
    ('6', 'Enter the amount of money you have: '),
    ('7', 'Invalid choice. Please enter a number between 0 and 6.')
])
def test_print_menu(choice, expected, capsys, monkeypatch):
    # Это подмена ввода пользователя на заданный выбор
    monkeypatch.setattr('builtins.input', lambda _: choice)
    # Это вызов основного цикла программы
    book_manager.main()
    # Это захват вывода на экран
    captured = capsys.readouterr()
    # Это утверждение, которое проверяет, что функция print выводит ожидаемый текст
    assert expected in captured.out
