def bold(func):
    def wrapper():
        return f"<b> {func()}</bold>"
    
    return wrapper

def italics(func):
    def wrapper():
        return f"<i> {func()}</i>"
    
    return wrapper




@bold
@italics
def say_hello():
    return "Hello, world!"

html= say_hello()
print(html)