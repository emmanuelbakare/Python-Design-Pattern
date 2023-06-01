# Context class to hold the program state
class Program:
    def __init__(self):
        self.variables = {}

    def set_variable(self, name, value):
        self.variables[name] = value

    def get_variable(self, name):
        return self.variables.get(name)
    

# Abstract Expression class
class Expression:
    def interpret(self, context):
        pass

# Terminal Expression class for variable assignment
class AssignmentExpression(Expression):
    def __init__(self, variable, value): 
        self.variable = variable
        self.value = value

    def interpret(self, context):
        context.set_variable(self.variable, self.value)

# Terminal Expression class for variable access
class VariableExpression(Expression):
    def __init__(self, variable):
        self.variable = variable

    def interpret(self, context):
        return context.get_variable(self.variable)
    
# Nonterminal Expression class for addition
class AddExpression(Expression):
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def interpret(self, context):
        value1 = self.expression1.interpret(context)
        value2 = self.expression2.interpret(context)
        return value1 + value2
    
# Client code
if __name__ == '__main__':
    context = Program()

    # Interpret and execute the program: x = 10; y = 5; z = x + y =15;

    AssignmentExpression("x", 10).interpret(context)
    AssignmentExpression("y", 5).interpret(context)

    add_expression  = AddExpression(VariableExpression("x"), VariableExpression("y") )
    add_value = add_expression.interpret(context)
    AssignmentExpression("z", add_value).interpret(context)

    result = VariableExpression("z").interpret(context)

    print("Result:",result) 
    print(context.__dict__)
