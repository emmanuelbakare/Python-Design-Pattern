from abc import ABC, abstractmethod

#===================IMPLEMENTATION================================
class Implementation(ABC): # COLOR
    @abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation): #RED
    def operation_implementation(self):
        print("ConcreteImplementationA operation executed.")

class ConcreteImplementationB(Implementation): #GREEN
    def operation_implementation(self):
        print("ConcreteImplementationB operation executed.")

#===================ABSTRACTION================================
class Abstraction(ABC):  #CAR
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        pass

class RefinedAbstraction(Abstraction): #TOYOTA
    def operation(self):
        print("RefinedAbstraction operation executed.")
        self.implementation.operation_implementation()

# Usage
implementation_a = ConcreteImplementationA()  #RED
implementation_b = ConcreteImplementationB()  #GREEN

refined_abstraction_a = RefinedAbstraction(implementation_a) #TOYOTA(RED)
refined_abstraction_a.operation()

print()

refined_abstraction_b = RefinedAbstraction(implementation_b) #TOYOTA(GREEN)
refined_abstraction_b.operation()

