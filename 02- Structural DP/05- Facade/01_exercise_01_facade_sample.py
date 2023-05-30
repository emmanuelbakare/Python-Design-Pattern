# Complex subsystem
class SubsystemA:
    def operationA1(self):
        print("Subsystem A Operation A1")

    def operationA2(self):
        print("Subsystem A Operation A2")

class SubsystemB:
    def operationB1(self):
        print("Subsystem B Operation B1")

    def operationB2(self):
        print("Subsystem B Operation B2")

# Facade
class Facade:
    def __init__(self):
        self.subsystemA = SubsystemA() 
        self.subsystemB = SubsystemB()

    def operation1(self):
        self.subsystemA.operationA1()
        self.subsystemB.operationB1()

    def operation2(self):
        self.subsystemB.operationB2() 
        self.subsystemA.operationA2()

# Client
if __name__ == '__main__':
    facade = Facade()
    facade.operation1()
    print()
    facade.operation2() 
