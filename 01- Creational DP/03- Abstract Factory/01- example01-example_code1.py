from abc import ABC, abstractmethod
####################################################
class Furniture(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass 

class Chair(Furniture):
    def display(self):
        return f"{self.quantity} Chair"

class Sofa(Furniture):
    def display(self):
        return f"{self.quantity} Sofa"
####################################################
class Electronic(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass 

class Radio(Electronic):
    def display(self):
        return f"{self.quantity} Radio(s)"
    
class Television(Electronic):
    def display(self):
        return f"{self.quantity} Television(s)"

####################################################
class Decoration(ABC):
    def __init__(self, quantity):
        self.quantity = quantity

    @abstractmethod
    def display(self):
        pass 

class FlowerVase(Decoration):
    def display(self):
        return f"{self.quantity} FlowerVase(s)"
    
class Chandalier(Decoration):
    def display(self):
        return f"{self.quantity} Chandalier"   

####################FACTORY#######################
class HomeFactory(ABC):
    @abstractmethod
    def furniture(self):
        pass 

    @abstractmethod
    def electronic(self):
        pass 

    @abstractmethod
    def decoration(self):
        pass 

class SmallHouse(HomeFactory):
    def furniture(self):
        return  Chair(4) 

    def electronic(self):
        return Radio(2) 

    def decoration(self):
        return FlowerVase(4) 

class BigHouse(HomeFactory):
    def furniture(self):
        return Sofa(10)  

    def electronic(self):
        return Television(7) 

    def decoration(self):
        return Chandalier(4)  


def client(factory:HomeFactory):
     print("Furniture : ", factory.furniture().display())
     print("Electronic : ", factory.electronic().display())
     print("Decoration : ", factory.decoration().display())
     print()

print("SMALL HOUSE".center(30,'*'))
client(SmallHouse())
print("BIG HOUSE".center(30,'*'))
client(BigHouse())



    