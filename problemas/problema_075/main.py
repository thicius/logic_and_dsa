# Método:

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        res_x = self.x + other.x
        res_y = self.y + other.y
        return '(%d, %d)' % (res_x, res_y)

# Teste:


point1 = Point(3.0, 4.0)
point2 = Point(5.0, 12.0)
print(point1 + point2)
