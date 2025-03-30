import math


class Point:
    def __init__(self, x, y, index=None):
        self.x = x
        self.y = y
        self.index = index

    def distance_to(self, other_point):
        diff_x = self.x - other_point.x
        diff_y = self.y - other_point.y
        return math.sqrt(diff_x ** 2 + diff_y ** 2)