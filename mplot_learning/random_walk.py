from random import choice


class RandomWalk:
    def __init__(self, points):
        """
        Constructor initialises start values.

        :param points: amount of points in path
        """
        self.x = [0]
        self.y = [0]
        self.points = points

    def fill_path(self):
        """
        This method creates path.
        """
        while len(self.x) < self.points:
            x_direction = choice([-1, 1])
            y_direction = choice([-1, 1])

            x_distance = choice(list(range(5)))
            y_distance = choice(list(range(5)))

            x_step = x_direction * x_distance
            y_step = y_direction * y_distance

            if x_step == 0 and y_step == 0:
                continue

            self.x.append(self.x[-1] + x_step)
            self.y.append(self.y[-1] + y_step)
