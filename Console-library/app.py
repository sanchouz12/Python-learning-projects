from utils import database
from utils.errors import ContentNotFound, EmptyDatabase

USER_CHOICE = """====================================
Enter 'a' to add a book
Enter 'l' to list all books
Enter 'r' to mark a book as read
Enter 'd' to delete a book
Enter 'q' to quit: """


def menu():
    user_input = input(USER_CHOICE)

    while user_input != "q":
        print("====================================")

        if user_input == "a":
            add_book()
        elif user_input == "l":
            list_books()
        elif user_input == "r":
            mark_book()
        elif user_input == "d":
            del_book()
        else:
            print("No such choice, try again")

        user_input = input(USER_CHOICE)


def add_book():
    name = input("Input name of the book you want to add: ")
    author = input("Input author of the book you want to add: ")

    database.add({
        "name": name,
        "author": author,
        "is_read": False
    })


def list_books():
    try:
        books = database.get_books()

        # printing in a bit nicer way
        read = "Yes" if books[0]['is_read'] == "True" else "No"
        print(f"Name - {books[0]['name']}\nAuthor - {books[0]['author']}\nIs read - {read}")

        for book in books[1:]:
            read = "Yes" if book['is_read'] == "True" else "No"
            print(f"\nName - {book['name']}\nAuthor - {book['author']}\nIs read - {read}")
    except EmptyDatabase:
        print(f"{EmptyDatabase.__name__}: Database is empty!")


def mark_book():
    name = input("Input name of the book you want to mark as read: ")

    try:
        database.mark(name)
    except ContentNotFound:
        print(f"{ContentNotFound.__name__}: Nothing found! Thy to check your spelling")
    except EmptyDatabase:
        print(f"{EmptyDatabase.__name__}: Database is empty!")


def del_book():
    name = input("Input name of the book you want to delete: ")

    try:
        database.remove(name)
    except ContentNotFound:
        print(f"{ContentNotFound.__name__}: Nothing found! Thy to check your spelling")
    except EmptyDatabase:
        print(f"{EmptyDatabase.__name__}: Database is empty!")


if __name__ == "__main__":
    menu()
