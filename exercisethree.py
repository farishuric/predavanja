class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


pt1 = Point(2,3)
pt2 = Point(5,6)
pt3 = Point(7,2)
result = pt1 + pt2 + pt3
print(result.x, result.y)
