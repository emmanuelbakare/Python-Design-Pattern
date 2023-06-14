
# Strategy  - abstract/interface defines interfaces for all strategies
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def operation(self) -> None:
        pass

# strategies - Implementation of strategy interface. Contains different algorithms/strategy
class ConcreteStrategy1(Strategy):
    def operation(self) -> None:
        print("Executing Concrete Strategy 1")

class ConcreteStrategy2(Strategy):
    def operation(self) -> None:
        print("Executing Concrete Strategy 2")


# context - the code that uses a strategy. it invoke the algorithm/strategy 
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def execute_strategy(self) -> None:
        self.strategy.operation()



# client - usage
strategy1 = ConcreteStrategy1()
strategy2 = ConcreteStrategy2()

context  = Context(strategy1)
context.execute_strategy() 

context.strategy = strategy2
context.execute_strategy()