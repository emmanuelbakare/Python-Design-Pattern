# Context class to hold the program state
class ConfigContext:
    def __init__(self):
        self.configurations = {}

    def set_configuration(self, key, value):
            self.configurations[key] = value

    def get_configuration(self, key):
        return self.configurations.get(key)
    

# Abstract Expression class
class ConfigExpression:
    def interpret(self, context):
        pass

# Terminal Expression class for configuration assignment
class AssignmentExpression(ConfigExpression):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def interpret(self, context):
        context.set_configuration(self.key, self.value)


# Nonterminal Expression class for configuration block
class BlockExpression(ConfigExpression):
    def __init__(self, expressions):
        self.expressions = expressions

    def interpret(self, context):
        for expression in self.expressions:
            expression.interpret(context)

# Client code
if __name__ == '__main__':
    context = ConfigContext()


    # Interpret and execute the configuration script
    config_script =BlockExpression([
        AssignmentExpression("username", "john_doe"),
        AssignmentExpression("password", "secret123"),
        BlockExpression([
            AssignmentExpression("host", "localhost"),
            AssignmentExpression("port", "8080")
        ])
    ])

    config_script.interpret(context)

     # Access and print the configurations
    # print("Username:", context.get_configuration("username"))
    # print("Password:", context.get_configuration("password"))
    # print("Host:", context.get_configuration("host"))
    # print("Port:", context.get_configuration("port")) 

    for key,value in context.configurations.items():
        print(f"{key}: {value}")


    
