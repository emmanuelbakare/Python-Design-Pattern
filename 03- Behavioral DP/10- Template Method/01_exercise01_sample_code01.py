##### Template Method Components #########
#1. abstract class -defines the overall algorithm /structure
#2. Template methods -  series of method calls that represent the steps of the algorithm
    #b. abstract methods - must be declare
    #b. Hook Methods - optional methods or default implementation for all subclasses

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.initialize()
        self.perform_algorithm()
        self.cleanup()

    def initialize(self):
        print("Initializing the algorithm.")

    @abstractmethod
    def perform_algorithm(self):
        pass

    def cleanup(self):
        print("Cleaning up after the algorithm.")


class ConcreteClass1(AbstractClass):
    def perform_algorithm(self):
        print("Performing Algorithm in ConcreteClass1")


class ConcreteClass2(AbstractClass):
    def perform_algorithm(self):
        print("Performing Algorithm in ConcreteClass2")

    def cleanup(self):
        print("Cleaning: ConcreteClass 2")

concrete_object1 = ConcreteClass1() 
concrete_object1.template_method()

print()
concrete_object2 = ConcreteClass2()
concrete_object2.template_method()