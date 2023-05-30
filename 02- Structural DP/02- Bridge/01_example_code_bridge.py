# Colored Shape 

from abc import ABC, abstractmethod 

#===================ABSTRACTION===================
class Shape(ABC):
    def __init__(self, color):
        self.color = color  

    @abstractmethod
    def shape_type(self):
        pass 

    def __str__(self):
        return f"This is a {self.color.name()} {self.shape_type()} " 

class Circle(Shape):
   def shape_type(self):
        return "Circle" 
   
class Square(Shape):
   def shape_type(self):
        return "Square" 
   
class Rectangle(Shape):
   def shape_type(self):
        return "Rectangle" 




#===================IMPLEMENTATION================================
class Color(ABC):
    
    @abstractmethod
    def name(self):
        pass 

class Red(Color):
    def name(self):
        return "Red"
    
class Green(Color):
    def name(self):
        return "Green"
    
class Blue(Color):
    def name(self):
        return "Blue"
    
class Yellow(Color):
    def name(self):
        return "Yellow"
    


red = Red()
blue = Blue()

circle = Circle(red)
blue_circle = Circle(blue)

print(circle)
print(blue_circle)

print(Square(Green()))
print(Rectangle(Yellow()))
print(Rectangle(Red()))