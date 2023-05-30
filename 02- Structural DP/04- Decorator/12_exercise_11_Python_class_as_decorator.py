class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self,*args, **kwargs):
        print("Before function...")
        result = self.func(*args, **kwargs)
        print("After function...")
        return result

@Decorator
def greeting():
    print("Hello, world")

greeting() 



