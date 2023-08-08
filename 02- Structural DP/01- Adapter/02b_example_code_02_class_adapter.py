class Service:
    def request(self):
        return "Get service from provider"
    
class Adaptee: 
    def complex_request(self):
        return "Get complex request from Service Provider"
    

class Adaptee2:
    def requested(self):
        return "Get REQUESTED service from provider"
    
class Target:
    def request(self):
        pass

class Adapter(Target, Adaptee, Adaptee2):
    # def __init__(self, adaptee):
    #     self.adaptee = adaptee

    def request(self):
        return f"Adaptee1: {self.complex_request()}\nAdaptee 2: {self.requested()}"
    

service= Service()
print(service.request())

adapter = Adapter()
print(adapter.request())