import pygal

from dice import Dice

def menu():
    """
    Main menu
    """
    while True:
        dices_count = get_dices_count()

        if dices_count:
            dices_sides = get_dices_sides(dices_count)

            if len(dices_sides):
                dices = []
                for num in range(dices_count):
                    dices.append(Dice(dices_sides[num]))

                rolls = get_rolls()

                if rolls:
                    results = []
                    for _ in range(rolls):
                        roll_sum = sum([x.roll() for x in dices])

                        results.append(roll_sum)

                    frequencies = []
                    dice_side_list = [x.sides for x in dices]
                    max_sum = sum(dice_side_list) + 1

                    for num in range(1, max_sum):
                        frequency = results.count(num)
                        frequencies.append(frequency)

                    visualize(frequencies, rolls, dice_side_list)

        exit_v = input(
            "======================\n"\
            "Input 'q' to exit\n"\
            "# "
        )

        if exit_v == "q":
            break

def get_dices_count():
    """
    Asks from a user for an amount of dices

    :return dices: amount of dices
    """
    dices_count = 0

    try:
        dices_count = int(input(
            "======================\n"\
            "Input amount of dices\n"\
            "# "
        ))
    except:
        print(
            "======================\n"\
            "Bad input"
        )
    
    return dices_count

def get_dices_sides(dices_count):
    """
    Asks from a user for an amount of all dices sides

    :param dices_count: amount of dices
    :return dices_sides: list of dices sides
    """
    dices_sides = []

    try:
        for num in range(1, dices_count + 1):
            count = int(input(
                "======================\n"\
                "Input amount of sides in {} dice\n"\
                "# ".format(num)
            ))

            if count > 2:
                dices_sides.append(count)
            else:
                raise ValueError()
    except:
        dices_sides.clear()

        print(
            "======================\n"\
            "Bad input"
        )
    
    return dices_sides

def get_rolls():
    """
    Asks from a user for an amount of dice rolls and validates it

    :return rolls: amount of dice rolls
    """
    rolls = 0

    try:
        rolls = int(input(
            "======================\n"\
            "Input amount of rolls\n"\
            "# "
        ))
    except:
        print(
            "======================\n"\
            "Bad input"
        )
    
    return rolls

def visualize(frequencies, size, dice_side_list):
    """
    Visualizes frequencies in a histogram

    :param frequencies: list of input values
    :param size: amount of experiments
    :param dice_side_list: list of all dices sides
    """
    hist = pygal.Bar()

    hist.title = "Results of rolling dice {} times".format(size)
    hist.x_labels = [str(x) for x in range(1, sum(dice_side_list) + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency"

    hist.add("D{}".format(dice_side_list), frequencies)
    hist.render_to_file("dice_visual.svg")

if __name__ == "__main__":
    menu()
