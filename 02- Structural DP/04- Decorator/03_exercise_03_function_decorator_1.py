def my_decorator(func):
    def wrapper():
        print("Before Hello...")
        func()
        print("After Hello...")
    return wrapper


@my_decorator 
def hello():
    print("Hello There!!!")  


hello()
