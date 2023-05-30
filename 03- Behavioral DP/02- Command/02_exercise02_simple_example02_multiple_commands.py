# Command interface
class Command: 
    def execute(self):
        pass

# Concrete Command 
class Hello1(Command):
    def execute(self):
        print("Hello, Command Pattern 1 !")

class Hello2(Command):
    def execute(self):
        print("Hello, Command Pattern 2!")

class Hello3(Command):
    def execute(self):
        print("Hello, Command Pattern 3!")

# Invoker 
class Invoker:
    def __init__(self, commands=[]):
        self.commands = commands

    def set_command(self, command):
        self.commands.append(command)

    def execute_command(self):
        for command in self.commands:
            command.execute()

# Client 
hello1 = Hello1()
hello2 = Hello2()
hello3 = Hello3()

invoker = Invoker()
invoker.set_command(hello1)
invoker.set_command(hello2)
invoker.set_command(hello3)

invoker.execute_command()

# invoker = Invoker([Hello1(),Hello2(),Hello3()])
# invoker.execute_command()  




    

    