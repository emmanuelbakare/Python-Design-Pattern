from abc import ABC, abstractmethod

class Text(ABC):
    def __init__(self, text):
        self.text = text 

    @abstractmethod
    def render(self):
        pass
    
class PlainText(Text):
    def render(self):
        return self.text 
    
class TextDecorator(Text):
    def __init__(self, component):
        self.component = component

    def render(self):
        return self.component.render() 

class Bold(TextDecorator):
    def render(self):
        return f"<b>{self.component.render()}</b>" 
      
class Italics(TextDecorator):
    def render(self):
        return f"<i>{self.component.render()}</i>" 

text = Italics(Bold(PlainText("Hello World")))

print(text.render())