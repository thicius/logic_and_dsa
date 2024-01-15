# Método:

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

# Teste:


point = Point()

point.__init__()
print(point.x, point.y)

point.__init__(3.0, 4.0)
print(point.x, point.y)
