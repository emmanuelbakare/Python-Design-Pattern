import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = None
        self._area = None
        self._circumference = None

    @property
    def diameter(self):
        if self._diameter is None:
            self._diameter = self.radius * 2
        return self._diameter
    
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
        return self._area 
    
    @property
    def circumference(self):
        if self._circumference is None:
            self._circumference = 2 * math.pi * self.radius
        return self._circumference
    




c1 = Circle(5)
print(f"Circle with radius {c1.radius} has diameter {c1.diameter}, area {c1.area}, and circumference {c1.circumference}.")

c2 = Circle(10)
print(f"Circle with radius {c2.radius} has diameter {c2.diameter}, area {c2.area}, and circumference {c2.circumference}.")
