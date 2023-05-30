class Target:
    def request(self):
        pass

class Adaptee:
    def specific_request(self):
        return "Specific request"


class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.specific_request() 
    

adaptee = Adaptee() 
adapter = Adapter(adaptee)

result = adapter.request()
print(result)