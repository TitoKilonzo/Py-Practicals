# ---- Polymorphism through method overriding ----------------------
class Shape:
    def area(self) -> float:
        raise NotImplementedError('Each shape must implement area()')

    def describe(self):
        print(f'{self.__class__.__name__}: area = {self.area():.2f} sq units')


class Circle(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, w, h): self.width = w; self.height = h
    def area(self): return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height): self.base = base; self.height = height
    def area(self): return 0.5 * self.base * self.height


# Polymorphic usage - same code, different behaviour!
shapes = [Circle(7), Rectangle(5, 8), Triangle(6, 4)]
for shape in shapes:
    shape.describe()   # Each calls ITS OWN area()

# Output:
# Circle:    area = 153.94 sq units
# Rectangle: area = 40.00 sq units
# Triangle:  area = 12.00 sq units

# The describe() method works for ALL shapes
# without knowing which specific shape it is!