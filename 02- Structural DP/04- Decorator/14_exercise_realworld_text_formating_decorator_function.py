# Text Formatting Implementation using Python Function Decorator

def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italics(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper 


@bold
@italics
def format_text(text):
    return text 


print(format_text("Hello, world!"))