import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_origin(self):
        xy = math.sqrt(self.x**2 + self.y**2)
        return xy


point = Point(5, 25)
print(point.distance_origin())
