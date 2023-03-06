import copy


class Prototype:

    def __init__(self):
        self._obj = {} 

    def register(self, name, obj):
        self._obj[name] = obj
    
    def unregister(self, name):
        del self._obj[name]

    def clone(self, name, **attrs):
        obj = None
        if self._obj:
            obj = copy.deepcopy(self._obj[name])
            obj.__dict__.update(attrs)
        
        return obj

class Adder:
    def __init__(self, num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2

    def area(self):
        return self.num1 + self.num2

add1= Adder(20,11)
print(add1.area())

prty = Prototype()

multi = prty.register("adder",add1)  

mult = prty.clone("adder", num1=23, num2=10)
mult2 = prty.clone("adder", num1=90, num2=40)

print(add1.__dict__)
print(mult.__dict__)

print("Add 1 area", add1.area(), 
      "Mult 1 Area", mult.area(),
       "Mult 2 Area", mult2.area() )



