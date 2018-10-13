class Point:

    def __init__(self, x, y):
        self.b = 2
        self.a = 3
        self.x = x
        self.y = y

    def add(self, other):
        if other.x != self.x:
            s = (other.y - self.y) / (other.x - self.x)
            x3 = s ** 2 - self.x - other.x
            y3 = self.y + s * (x3 - self.x)
            self.x = x3
            self.y = y3

    def check_if_valid(self):
        return (self.y ** 2 - self.x ** 3 - 3 * self.x - 2) < 0.001


point1 = Point(2, 4)
point2 = Point(-0.596, 0)

print(point1.check_if_valid())
print(point2.check_if_valid())

point1.add(point2)
print(point1.x)
print(point1.y)

print(point1.check_if_valid())
