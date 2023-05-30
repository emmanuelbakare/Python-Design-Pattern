from abc import ABC, abstractmethod

# Receiver
class TV:
    def turn_on(self):
        print("TV is turned on.")

    def turn_off(self):
        print("TV is turned off.")

####################################################

# Command interface
class Command(ABC):
    def __init__(self, tv):
        self._tv = tv

    @abstractmethod
    def execute(self):
        pass
        
class TurnOnCommand(Command):
    def execute(self):
        self._tv.turn_on()

class TurnOffCommand(Command):
    def execute(self):
        self._tv.turn_off()

####################################################

# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None 
    
    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

####################################################


# Client code
tv = TV()

turn_on_command = TurnOnCommand(tv)
turn_off_command = TurnOffCommand(tv)

remote_control = RemoteControl()

remote_control.set_command(turn_on_command)
remote_control.press_button() 

remote_control.set_command(turn_off_command)
remote_control.press_button() 

    
