# state
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def do_action(self, context):
        pass

class StateA(State):
    def do_action(self, context):
        print("State A: Performing action...")
        context.state = StateB()

class StateB(State):
    def do_action(self, context):
        print("State B: Performing action...")
        context.state = StateC()

class StateC(State):
    def do_action(self, context):
        print("State C: Performing action...")
        context.state = StateA()

# context       
class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        self.state.do_action(self)



context = Context()
context.request()
context.request()
context.request()
context.request()
context.request()