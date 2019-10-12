print("This program uses files, so all output will be in 'friends.txt'")


def menu():
    while True:
        friends = get_input()

        if friends:
            compare_data(friends)

        stop = input("Would you like to exit (y/n)? ")

        if stop != "n":
            break


def get_input():
    user_input = input("Input 3 friend's names (separate by comma): ")
    input_data = set(user_input.split(", "))

    if len(input_data) != 3:
        print("Invalid input")
        return 0
    else:
        return input_data


def compare_data(friends):
    r_file = open("nearby_people.txt", "r")

    read_data = set([line.strip() for line in r_file.readlines()])

    r_file.close()

    near = friends.intersection(read_data)

    w_file = open("friends.txt", "w")

    if not len(near):
        w_file.write("The are no friends nearby")
    else:
        for friend in near:
            w_file.write(friend + "\n")

    w_file.close()


if __name__ == "__main__":
    menu()
