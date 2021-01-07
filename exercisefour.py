class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    
pt1 = Point(2,3)
pt2 = Point(2,3)
print(pt1 == pt2)