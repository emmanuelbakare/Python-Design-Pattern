from abc import ABC, abstractmethod

class Product(ABC): # Vehicle
    @abstractmethod
    def operation(self):
        pass

class ConcreteProductA(Product): #e.g. Car
    def operation(self):
        return "ConcreteProductA operation."

class ConcreteProductB(Product):  # e.g. Bicycle
    def operation(self):
        return "ConcreteProductB operation."  


class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass  

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


#client code
creator_a = ConcreteCreatorA()
product_a = creator_a.factory_method()
print(product_a.operation()) 

creator_b = ConcreteCreatorB()
product_b = creator_b.factory_method()
print(product_b.operation())



