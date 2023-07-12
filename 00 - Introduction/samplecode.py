from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__
    
class Cat(Animal):
    def sound(self):
        return "Meow"
    
class Dog(Animal):
    def sound(self):
        return "Woof"
    
class Client:
    def __init__(self,animal:Animal):
        self.animal = animal 
        
    def say(self):
        print(f"{self.animal} will say {self.animal.sound()}")

cat = Client(Cat())
dog = Client(Dog())
cat.say()
dog.say()

        