class Request:
    def __init__(self, amount):
        self.amount = amount

# handler interface 
class Handler:
    def __init__(self, successor=None):
        self.successor = successor
    
    def handle_request(self, request):
        pass


class Manager(Handler):
    def handle_request(self, request):
        if request.amount <= 1000:
            print("Manager approves the request with amount:", request.amount)
        elif self.successor is not None:
            self.successor.handle_request(request)

class Director(Handler):
    def handle_request(self, request):
        if request.amount <= 5000:
            print("Director approves the request with amount:", request.amount)
        elif self.successor is not None:
            self.successor.handle_request(request)

class CEO(Handler):
    def handle_request(self, request):
        if request.amount <= 10000:
            print("CEO approves the request with amount:", request.amount)
        elif self.successor is not None:
            self.successor.handle_request(request)
        else:
            print("Request exceeds approval limit.")

# Creating the chain
# manager = Manager()
# director = Director()
# ceo = CEO()

# manager.successor = director
# director.successor = ceo

# # Handling requests
# request1 = Request(90000)
# manager.handle_request(request1)  \

handler = Manager(Director(CEO()))
request1 = Request(19900)
handler.handle_request(request1)  