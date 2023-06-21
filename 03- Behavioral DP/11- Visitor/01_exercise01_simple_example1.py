

#element1 
#behavior1, behavior2 -visitor

from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit(self, element):
        pass

# Concrete Visitor 1
class ConcreteVisitor1(Visitor):
    def visit(self, element):
        element.operation1()
        # Perform specific operation on Element
        print("more stuff going on with visitor 1")

# Concrete Visitor 2
class ConcreteVisitor2(Visitor):
    def visit(self, element):
        element.operation2()
        # Perform different operation on Element
        print("more stuff going on with visitor 2")
        
        


# Element interface
class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ConcreteElementA(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation1(self):
        print("ConcreteElementA is performing Operation 1")

    def operation2(self):
        print("ConcreteElementA is performing Operation 2")


class ConcreteElementB(Element):
    def accept(self, visitor):
        visitor.visit(self)

    def operation1(self):
        print("ConcreteElementB is performing Operation 1")

    def operation2(self):
        print("ConcreteElementB is performing Operation 2")

    

# Client code
if __name__ == '__main__':
    # Create elements
    element_a = ConcreteElementA()
    element_b = ConcreteElementB()

    # Create visitors
    visitor1 = ConcreteVisitor1()
    visitor2 = ConcreteVisitor2()

    # Accept visitors
    element_a.accept(visitor1)
    element_a.accept(visitor2) 

    element_b.accept(visitor1)
    element_b.accept(visitor2)



    