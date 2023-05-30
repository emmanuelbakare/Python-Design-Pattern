def greetings(cls):
    cls.greet = lambda self: f"Hello {self}"
    return cls

@greetings
class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    
  


p = Person("Matthew")

print(p.greet())