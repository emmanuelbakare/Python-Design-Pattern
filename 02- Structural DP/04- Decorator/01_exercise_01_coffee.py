''' Decorator Design Pattern

- component(Abstract/interface)
    **concrete component(component)

- Decorator(Abstract/interface)
    **concrete decorator(Decorator)

- Client
'''
from abc import ABC, abstractmethod

class Coffee(ABC):

    @abstractmethod
    def get_cost(self):
        pass 
    
    @abstractmethod
    def get_description(self):
        pass 

class PlainCoffee(Coffee):
    def get_cost(self):
        return 2
    
    def get_description(self):
        return "Plain Coffee"

class CoffeeDecorator(Coffee):

    def __init__(self, coffee):
        self.coffee = coffee

    def get_cost(self):
        return self.coffee.get_cost()
    
    def get_description(self):
        return self.coffee.get_description()

class Milk(CoffeeDecorator):

    def get_cost(self):
        return self.coffee.get_cost() + 1.99 
    
    def get_description(self):
        return self.coffee.get_description() + "==> Milk"

class Sugar(CoffeeDecorator):

    def get_cost(self):
        return self.coffee.get_cost() + 2
    
    def get_description(self):
        return self.coffee.get_description() + "==> Sugar"
    

coffee = PlainCoffee()
coffee = Milk(coffee)
coffee = Sugar(coffee)

print(f"Mix: {coffee.get_description()}\nTotal: ${coffee.get_cost()}")