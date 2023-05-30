def repeat(num):
    def repeat_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs) 
        return wrapper 
    return repeat_decorator


@repeat(3)
def hello(text):
    print(text)


hello("Hello world")
 