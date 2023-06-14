from abc import ABC, abstractmethod

class StockMarket:
    def __init__(self):
        self._observers = []
        self._stocks = {}

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def add_stock(self, symbol, price):
        self._stocks[symbol] = price
        self.notify(symbol)

    def update_stock_price(self, symbol, new_price):
        self._stocks[symbol] = new_price
        self.notify(symbol)

    def notify(self, symbol):
        for observer in self._observers:
            observer.update(symbol, self._stocks[symbol])

class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass

class Investor(Observer):
    def __init__(self, name):
        self._name = name

    def update(self, symbol, price):
        print(f"Investor {self._name}: Stock {symbol} price is now {price}")


# Usage example
stock_market = StockMarket()

investor1 = Investor("John")
investor2 = Investor("Alice")

stock_market.attach(investor1)
stock_market.attach(investor2)

stock_market.add_stock("AAPL", 150.25) 
print()
stock_market.add_stock("GOOGL", 2500.75)
print()

stock_market.update_stock_price("AAPL", 155.50)

stock_market.detach(investor1)

print()
stock_market.update_stock_price("AAPL", 165.70)

