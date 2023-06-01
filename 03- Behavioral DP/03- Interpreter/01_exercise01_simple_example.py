# Abstract Expression class
class Expression:
    def interpret(self):
        pass

class Number(Expression):  # Terminal Expression
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Addition(Expression): # NonTerminal Expression
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self):
        return self.expression1.interpret() + self.expression2.interpret()

class Subtraction(Expression): # NonTerminal Expression
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self):
        return self.expression1.interpret() - self.expression2.interpret()


exppression = Addition(Number(5), Number(2))
# print(exppression.interpret()) 

# Create the expression tree: 5 + (3 - 2)

expression = Addition(
    Number(5),
    Subtraction(
        Number(3),
        Number(2)
    )
)

print(expression.interpret())

