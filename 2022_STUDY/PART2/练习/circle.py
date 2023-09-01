class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radium(self):
        return self.radius

    def distance(self, x, y):
        distance = (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y)
        return distance ** 0.5

    def relation(self, cir):
        distance = self.distance(cir.get_x(), cir.get_y())
        if distance > abs(self.radius + cir.get_radium()):
            return "相离"
        elif distance == abs(self.radius + cir.get_radium()):
            return "相切"
        elif distance == abs(self.radius - cir.get_radium()):
            return "相切"
        else:
            return "相交"


circle1 = Circle(0, 0, 1)
circle2 = Circle(3, 0, 2)
print(float(circle2.area()))
print(circle1.relation(circle2))
