import matplotlib.pyplot as plt

from random_walk import RandomWalk

def menu():
    """
    Main menu of the program.
    """
    quit_v = ""
    points = 0

    while quit_v != "q":
        points = get_points()

        if points:
            path = RandomWalk(points)
            path.fill_path()

            plt.figure(figsize = (10, 6))

            option = input(
                "================================================\n"\
                "Input 'd' to plot using dots\n"\
                "Input 'l' to plot using lines\n"\
                "================================================\n"
            )

            if option == "d":
                plt.scatter(path.x, path.y, s = 5, c = list(range(points)), cmap = plt.cm.seismic)
                show(path)
            elif option == "l":
                plt.plot(path.x, path.y, linewidth = 1)
                show(path)
            else:
                print(
                    "Bad input\n"\
                    "================================================\n"
                )
        
        quit_v = input(
            "================================================\n"\
            "Input 'q' to quit or something else to countinue\n"\
            "================================================\n"
        )

def get_points():
    """
    Asks for a user to input amount of points and validates it.

    :return points: amount of points in path
    """
    points = 0

    try:
        points = int(input(
            "================================================\n"\
            "Input amount of points in random walk path\n"\
            "================================================\n"
        ))
    except:
        print(
            "Bad input\n"\
            "================================================\n"
        )
    
    return points

def show(path):
    """
    Shows points in path.

    :param path: RandomWalk object
    """
    plt.scatter(path.x[0], path.y[0], s = 80, c = "green")
    plt.scatter(path.x[-1], path.y[-1], s = 80, c = "yellow")

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

if __name__ == "__main__":
    menu()
