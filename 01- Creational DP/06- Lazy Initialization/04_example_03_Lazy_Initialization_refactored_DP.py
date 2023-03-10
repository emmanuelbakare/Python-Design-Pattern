import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.__area = None

    def area(self):
        if self.__area is None:
            print("printing out area")
            self.__area =math.pi * self.radius ** 2
        return self.__area


if __name__=="__main__":
    circle = Circle(5)
    print(circle.area())

    print(circle.area())
    print(circle.area())

