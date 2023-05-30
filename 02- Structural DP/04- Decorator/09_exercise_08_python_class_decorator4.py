
def word(text):
    def decor(cls):
        cls.say = lambda self: f"{self} says {text}"
        return cls
    return decor

@word("We are going out")
class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    
p = Person("Luke")

print(p.say()) 