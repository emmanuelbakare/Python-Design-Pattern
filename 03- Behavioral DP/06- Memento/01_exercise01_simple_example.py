class Editor:
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text

    def get_content(self):
        return self.content
    
    def create_memento(self):
        return Memento(self.content)
    
    def restore_memento(self, memento):
        self.content = memento.get_saved_content()

class Memento:
    def __init__(self, content):
        self.saved_content = content

    def get_saved_content(self):
        return self.saved_content
    
class Caretaker:
    def __init__(self):
        self.mementos = []

    def add_memento(self, memento):
        self.mementos.append(memento)

    def get_memento(self, index):
        return self.mementos[index]


# Usage example
editor = Editor()
caretaker = Caretaker()

editor.add_text("Hello, ")
caretaker.add_memento(editor.create_memento())


editor.add_text("World!")
caretaker.add_memento(editor.create_memento())

editor.add_text(" Goodbye!") 
caretaker.add_memento(editor.create_memento())
print(editor.get_content())  

editor.restore_memento(caretaker.get_memento(1))
print(editor.get_content()) 

editor.restore_memento(caretaker.get_memento(0))
print(editor.get_content()) 

editor.restore_memento(caretaker.get_memento(2))
print(editor.get_content()) 