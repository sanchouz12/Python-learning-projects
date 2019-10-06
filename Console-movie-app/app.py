movies = []


def menu():
    while True:
        print("===============================")

        user_input = input(
            "Input 'a' to add a new movie\n"
            "Input 'l' to see all movies\n"
            "Input 'f' to find a movie\n"
            "Input 'q' to quit: "
        )

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies(movies)
        elif user_input == 'f':
            show_movies(find_movie())
        elif user_input == 'q':
            break
        else:
            print("No such operation")


def add_movie():
    print("===============================")

    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie year: "))

    movies.append({
        'name': name,
        'director': director,
        'year': year
    })


def show_movies(movies_list):
    if len(movies):
        for movie in movies_list:
            print("===============================")
            print(f"Name: {movie['name']}")
            print(f"Director: {movie['director']}")
            print(f"Year: {movie['year']}")
    else:
        print("Nothing found")


def find_movie():
    print("===============================")

    finder = input("Input property of the movie: ")
    expected = input("Input what are you searching for: ")

    found = []
    if finder == 'year':
        expected = int(expected)

    for movie in movies:
        if movie[finder] == expected:
            found.append(movie)

    return found


if __name__ == "__main__":
    menu()
