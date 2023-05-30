#receiver 
class Greet:
    def spanish(self):
        print("Hola")

    def english(self):
        print("Hello")

# Command interface
class Command:
    def __init__(self, greeting):
        self._greet = greeting 
        
    def execute(self):
        pass

# Concrete Command 
class Hello1(Command):
    def execute(self):
        self._greet.spanish()

class Hello2(Command):
    def execute(self):
        self._greet.english()



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

greet = Greet()
hello1 = Hello1(greet)
hello2 = Hello2(greet)

invoker = Invoker()
invoker.set_command(hello1)
invoker.set_command(hello2)

invoker.execute_command() 

# invoker = Invoker([
#         Hello1(),
#         Hello2(),
#         Hello3()
#     ])

# invoker.execute_command()   




    

    