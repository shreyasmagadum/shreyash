class Circle:
    pi = 3.14  # Class attribute

    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi

    def calculate_area(self):
        return self.pi * (self.radius ** 2)

Circle.set_pi(3.14159)

circle1 = Circle(5)
print(circle1.calculate_area())