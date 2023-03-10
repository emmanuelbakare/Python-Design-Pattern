import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("printing out area")
        return math.pi * self.radius ** 2


if __name__=="__main__":
    circle = Circle(5)
    print(circle.area())

    print(circle.area())
    print(circle.area())

 


 