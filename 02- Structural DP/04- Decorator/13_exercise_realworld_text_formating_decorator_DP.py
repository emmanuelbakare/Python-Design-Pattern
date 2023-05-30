class Text:
    def __init__(self, text):
        self.text = text 

    def render(self):
        return self.text 
    
class TextDecorator:
    def __init__(self, component):
        self.component = component
    
    def render(self):
        return self.component.render()

class Bold(TextDecorator):
    def render(self):
        return f"<b>{self.component.render()} </b>"

class Italics(TextDecorator):
    def render(self):
        return f"<i>{self.component.render()} </i>"
    
text = Italics(Bold(Text("Hello, World!")))
# bold_text = Bold(text)



print(text.render())
# print(bold_text.render())
 
    

