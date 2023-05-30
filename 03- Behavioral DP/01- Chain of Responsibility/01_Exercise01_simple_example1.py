from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor= None):
        self.successor = successor

    @abstractmethod
    def request_handler(self, request):
        pass


class ConcreteHandler1(Handler):
    def request_handler(self, request):
        if request =='A':
            print(F'{request} is handled at Handler 1')
        elif self.successor is not None:
            print('Hander 1 is not handling this request')
            self.successor.request_handler(request)


class ConcreteHandler2(Handler):
    def request_handler(self, request):
        if request =='B':
            print(F'{request} is handled at Handler 2')
        elif self.successor is not None:
            print('Hander 2 is not handling this request')
            self.successor.request_handler(request)

class ConcreteHandler3(Handler):
    def request_handler(self, request):
        if request =='C':
            print(F'{request} is handled at Handler 3')
        elif self.successor is not None:
            self.successor.request_handler(request)
        else:
            print('Hander 3 is not handling this request')
            print('Request handling Terminated')


# handler1 = ConcreteHandler1()
# handler2 = ConcreteHandler2()
# handler3 = ConcreteHandler3()

# handler1.successor = handler2
# handler2.successor = handler3 

handler1 = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3()))

handler1.request_handler('B') 