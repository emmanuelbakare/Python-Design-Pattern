
def word(text):
    def decor(cls):
        def funct1(self):
            return  f"{self} says {text}"
        
        def funct2(self):
            return f"Hello {self}"
        cls.greet = funct2
        cls.say = funct1
        return cls
    return decor 

@word("Go to school")
class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    
p = Person("Luke")

print(p.say()) 
print(p.greet())

print(Person.__dict__)

