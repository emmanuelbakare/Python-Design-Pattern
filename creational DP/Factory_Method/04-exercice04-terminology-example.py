from abc import ABC, abstractmethod


class Creator(ABC):
    
    @abstractmethod
    def create_product_factory(self):
        pass

class ConcreteCreatorA(Creator):
    def create_product_factory(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def create_product_factory(self):
        return ConcreteProductB()

class Product(ABC):

    @abstractmethod
    def do_something(self):
        pass

class ConcreteProductA(Product): 
    def do_something(self):
        print("Doing something with Product A")

class ConcreteProductB(Product):
    def do_something(self):
        print("Doing something with Product B")

class Client:
    def __init__(self, creator):
        self._product = creator.create_product_factory()

    def do_something(self):
        self._product.do_something()

if __name__ == "__main__":
    concreteProduct = Client(ConcreteCreatorA())
    concreteProduct.do_something()

    concreteProduct = Client(ConcreteCreatorB())
    concreteProduct.do_something()
