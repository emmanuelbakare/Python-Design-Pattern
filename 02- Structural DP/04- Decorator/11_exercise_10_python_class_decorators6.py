def square_decor(func):
    def wrapper(self):
        return func(self) ** 2
    return property(wrapper)

class MyClass:
    def __init__(self, x):
        self.x = x

    @square_decor
    def squared(self):
        return self.x
    
obj = MyClass(5)
print(obj.squared)