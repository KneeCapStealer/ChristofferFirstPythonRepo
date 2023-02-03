import math


# Vec2 classen er lavet i collab med Atle
class Vec2:
    x: float = 0
    y: float = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # define overload for + operator
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    # define overload for - operator
    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    # define overload for == operator
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # define overload for != operator
    def __ne__(self, other):
        return self.x != other.m_x and self.y != other.y

    def __str__(self):
        return f'[x: {self.x}, y: {self.y}]'

    # here are real functions
    def normalize(self, other):
        return Vec2(self.x / self.length(), self.y / self.length())
