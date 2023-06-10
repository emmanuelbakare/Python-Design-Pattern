class DocumentMemento: #memento
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content
    
class Document: #originator
    def __init__(self):
        self.content = ""
    
    def add_text(self, text):
        self.content += text

    def get_content(self):
        return self.content
    
    def create_memento(self): #save_content
        return DocumentMemento(self.content)
    
    def restore_memento(self, memento):
        self.content = memento.get_content()

class DocumentEditor: #caretaker
    def __init__(self, document):
        self.document = document
        self.mementos = []

    def add_text(self, text):
        self.document.add_text(text)

    def save(self):
        memento = self.document.create_memento()
        self.mementos.append(memento)
        print("Document saved.")

    def undo(self):
        if len(self.mementos) > 0:
            memento = self.mementos.pop()
            self.document.restore_memento(memento)
            print("Undo operation successful.")
        else:
            print("No more undo operations available.")


# Usage example
document = Document()
editor = DocumentEditor(document)

editor.add_text("Hello, ")
editor.save()

editor.add_text("World!")
editor.save()

print("Current Content:", editor.document.get_content())

editor.undo()
print("Content after Undo:", editor.document.get_content())

editor.undo()
print("Content after Undo:", editor.document.get_content())


editor.undo()
print("Content after Undo:", editor.document.get_content())


 


    
