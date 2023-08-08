class Service:
    def request(self):
        return "Get service from provider"
    
class Adaptee: 
    def complex_request(self):
        return "Get complex request from Service Provider"
    

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return self.adaptee.complex_request()
    

service= Service()
print(service.request())

adapter = Adapter(Adaptee())
print(adapter.request())