from random import randint

class Dice:
    """
    Class representing a dice
    """
    def __init__(self, sides = 6):
        """
        :param sides: amount of sides in a dice
        """
        self.sides = sides

    def roll(self):
        """
        :return random value from 1 to amount of sides
        """
        return randint(1, self.sides)
