# Método:

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def add_point(self, other):
        res_x = self.x + other.x
        res_y = self.y + other.y
        return '(%d, %d)' % (res_x, res_y)

    def add_tuple(self, tup):
        res_x = self.x + tup[0]
        res_y = self.y + tup[1]
        return '(%d, %d)' % (res_x, res_y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

# Teste:


point1 = Point(3.0, 4.0)
point2 = Point(5.0, 12.0)
print(point1 + point2)

point3 = Point(7.0, 24.0)
tup = 9.0, 40.0
print(point3 + tup)
