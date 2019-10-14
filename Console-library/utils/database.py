from utils.errors import ContentNotFound, EmptyDatabase

books_file = "books.txt"


def add(content):
    with open(books_file, "a") as file:
        file.write(f"{content['name']},{content['author']},{content['is_read']}\n")


def get_books():
    try:
        with open(books_file, "r") as file:
            data = [line.strip().split(",") for line in file.readlines()]

            if data:
                return [  # [ [name, author, is_read], [name, author, is_read] ]
                    {
                        "name": item[0],
                        "author": item[1],
                        "is_read": item[2]
                    }
                    for item in data
                ]
            else:
                raise EmptyDatabase()
    except FileNotFoundError:
        _create_data_table()


def mark(name):
    books = get_books()
    is_found = False

    if len(books):
        for book in books:
            if book['name'] == name:
                book['is_read'] = "True"
                is_found = True

                _save_all(books)
                break

        if not is_found:
            raise ContentNotFound()
    else:
        raise EmptyDatabase()


def remove(name):
    books = get_books()
    is_found = False

    if len(books):
        for book in books:
            if book['name'] == name:
                books.remove(book)
                is_found = True

                _save_all(books)
                break

        if not is_found:
            raise ContentNotFound()
    else:
        raise EmptyDatabase()


def _save_all(books):
    with open(books_file, "w") as file:
        for item in books:
            file.write(f"{item['name']},{item['author']},{item['is_read']}\n")


def _create_data_table():
    with open(books_file, "w"):
        pass

    print("File wasn't found, created one")
