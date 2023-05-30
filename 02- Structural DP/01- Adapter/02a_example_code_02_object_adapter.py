class Adaptee:
    def specific_request(self):
        return "Specific request"

class Target:
    def request(self):
        return "Target request"
    
class Adapter:
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Adapter request ({self._adaptee.specific_request()})"
    
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request()) 