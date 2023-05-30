class Adaptee:
    def specific_request(self):
        return "Specific request"
    
class Target:
    def request(self):
        return "Target request"

class Adapter(Adaptee, Target):
    def request(self):
        return f"Adapter request ({self.specific_request()})"

adapter = Adapter()
print(adapter.request())