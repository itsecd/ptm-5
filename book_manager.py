books = []

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

def remove_book(title):
    global books
    books = [book for book in books if book['title'] != title]

def sort_by_release_date():
    return sorted(books, key=lambda x: x['release_date'], reverse=True)

def sort_by_pages():
    return sorted(books, key=lambda x: x['pages'])

def group_by_genre():
    genres = {}
    for book in books:
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1
    return genres

def count_books_affordable(amount):
    return [book for book in books if book['cost'] <= amount]

def print_menu():
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Sort by release date")
    print("4. Sort by pages")
    print("5. Group by genre")
    print("6. Count books affordable")
    print("0. Exit")

# Пример использования функций
while True:
    print_menu()
    choice = input("Enter your choice (0-6): ")

    if choice == "0":
        print("Goodbye!")
        break
    elif choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        pages = int(input("Enter number of pages: "))
        release_date = input("Enter release date (YYYY-MM-DD): ")
        cost = float(input("Enter cost: "))
        genre = input("Enter genre: ")
        add_book(title, author, pages, release_date, cost, genre)
    elif choice == "2":
        title = input("Enter the title of the book to remove: ")
        remove_book(title)
    elif choice == "3":
        print("Books sorted by release date:")
        print(sort_by_release_date())
    elif choice == "4":
        print("Books sorted by pages:")
        print(sort_by_pages())
    elif choice == "5":
        print("Books grouped by genre:")
        print(group_by_genre())
    elif choice == "6":
        amount = float(input("Enter the amount of money you have: "))
        print("Books affordable with ${}: {}".format(amount, count_books_affordable(amount)))
    else:
        print("Invalid choice. Please enter a number between 0 and 6.")
