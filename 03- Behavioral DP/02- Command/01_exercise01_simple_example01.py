# Command interface
class Command: 
    def execute(self):
        pass

# Concrete Command 
class HelloCommand(Command):
    def execute(self):
        print("Hello, Command Pattern!")

# Invoker 
class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self):
        self.command.execute()

# Client 

hello_command = HelloCommand()
invoker = Invoker()
invoker.set_command(hello_command)
invoker.execute_command()  




    

    