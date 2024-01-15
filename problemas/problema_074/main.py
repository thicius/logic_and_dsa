# Método:

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)

# Teste:


obj = Point(5.0, 12.0)
print(obj)
