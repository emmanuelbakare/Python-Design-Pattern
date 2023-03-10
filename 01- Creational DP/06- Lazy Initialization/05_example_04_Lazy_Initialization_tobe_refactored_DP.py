import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = math.pi * (radius ** 2)
        self.circumference = 2 * math.pi * radius

c1 = Circle(5)
print(f"Circle with radius {c1.radius} has diameter {c1.diameter}, area {c1.area}, and circumference {c1.circumference}.")

c2 = Circle(10)
print(f"Circle with radius {c2.radius} has diameter {c2.diameter}, area {c2.area}, and circumference {c2.circumference}.")
