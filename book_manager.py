books = []

# Функция для добавления книги
def add_book(title, author, pages, release_date, cost, genre):
    book = {
        'title': title,
        'author': author,
        'pages': pages,
        'release_date': release_date,
        'cost': cost,
        'genre': genre
    }
    books.append(book)

# Функция для удаления книги
def remove_book(title):
    global books
    books = [book for book in books if book['title'] != title]

# Функция для сортировки книг по новизне
def sort_by_release_date():
    return sorted(books, key=lambda x: x['release_date'], reverse=True)

# Функция для сортировки книг по количеству страниц
def sort_by_pages():
    return sorted(books, key=lambda x: x['pages'])

# Функция для группировки книг по жанрам
def group_by_genre():
    genres = {}
    for book in books:
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1
    return genres

# Функция для расчета, сколько книг и сколько можно будет купить имея на руках N денег
def count_books_affordable(amount):
    return [book for book in books if book['cost'] <= amount]

# Пример использования функций
add_book('Book1', 'Author1', 300, '2022-01-01', 20.0, 'Fiction')
add_book('Book2', 'Author2', 250, '2022-02-15', 15.0, 'Mystery')
add_book('Book3', 'Author3', 400, '2022-03-20', 25.0, 'Fantasy')

print("Books sorted by release date:")
print(sort_by_release_date())

print("\nBooks sorted by pages:")
print(sort_by_pages())

print("\nBooks grouped by genre:")
print(group_by_genre())

print("\nBooks affordable with $30:")
print(count_books_affordable(30.0))
