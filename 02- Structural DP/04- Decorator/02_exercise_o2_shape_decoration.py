# Shape Decorator  e.g Red Rectangle 

from abc import ABC, abstractmethod

class Shape(ABC):
     
     @abstractmethod
     def draw(self):
          pass

class Rectangle(Shape):
     
     def draw(self):
          print("Drawing a Rectangle.")

class ShapeDecorator(Shape):
    def __init__(self, shape):
        self.shape = shape

    def draw(self):
        return self.shape.draw()  

class RedShapeDecorator(ShapeDecorator):
     
    def draw(self):
        self.shape.draw()
        self.red_color() 

    def red_color(self):
        print(f"Painting {self.shape.__class__.__name__} Red")

class BlueShapeDecorator(ShapeDecorator):

    def draw(self):
        self.shape.draw()
        self.blue_color() 

    def blue_color(self):
        print(f"Painting  {self.shape.__class__.__name__} Blue")

rectangle = Rectangle()
red_rectangle = RedShapeDecorator(Rectangle())
blue_rectangle = BlueShapeDecorator(Rectangle())


rectangle.draw()

print("Colored Shape".center(30,"*"))
red_rectangle.draw()
print()
blue_rectangle.draw()


     
