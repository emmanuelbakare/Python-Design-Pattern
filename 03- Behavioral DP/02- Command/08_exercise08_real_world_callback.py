# Command interface
class Command:
    def execute(self):
        pass

# Concrete command
class CallbackCommand(Command):
    def __init__(self, callback):
        self.callback = callback

    def execute(self):
        self.callback()


# Invoker
class Invoker:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def execute_commands(self):
        for command in self.commands:
            command.execute()


# Client code
def callback1():
    print("Callback function executed!") 

def callback2():
    print("Making another call back")     

# Create an instance of the Invoker
invoker = Invoker()

callback_command1 = CallbackCommand(callback1)
callback_command2 = CallbackCommand(callback2)

# Add the command to the invoker
invoker.add_command(callback_command1)
invoker.add_command(callback_command2)

invoker.execute_commands()

    