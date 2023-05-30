# reciever 
class Document:
    def __init__(self, content=""):
        self.content = content
        self.undo =[]

    def add_content(self, text):
        self.content += text
        self.undo.append(text) 

    # Hello World 
    # Great  -> "Hello Great World"
    # insert(5,' Great')
    def insert(self, pos =0, text=''):
        if len(text) > 0:
            new_content = self.content[:pos] + text + self.content[pos:]   #Hello Great World
            self.content = new_content
            self.undo.append(text) 

    def cut(self,start=0,end=0):
        cut_content = self.content[start:end]
        new_content = self.content[:start]+self.content[end:]
        self.content = new_content
        self.undo.append(cut_content)

#################################################################
# command
class Command:
    def execute(self):
        pass 
    
    def undo(self):
        pass
    

## ADD Command    
class AddContentCommand(Command):
    def __init__(self, document, text_to_add=''):
        self.document = document
        self.text = text_to_add

    def execute(self):
        self.document.add_content(self.text) 

    def undo(self):
        to_remove= self.document.undo.pop()
        content = self.document.content
        self.document.content = content.replace(to_remove, '')

## CUT Command       
class CutContentCommand(Command):
    def __init__(self, document, start, end):
        self.document = document
        self.start = start
        self.end = end 
       
    def execute(self):
        self.document.cut(start= self.start, end= self.end)

    def undo(self):
        content = self.document.content
        undo_content = self.document.undo.pop()
        self.document.content = content[:self.start]+undo_content+content[self.start:]

## Insert Command   
class InsertContentCommand(Command):
    def __init__(self, document,  pos=0, text=''):
        self.document = document
        self.pos = pos 
        self.text = text

    def execute(self):
        self.document.insert(pos = self.pos, text=self.text)

    def undo(self):
        content = self.document.content # get current content
        text = self.document.undo.pop() # text to undo
        self.document.content = content[:self.pos]+content[self.pos+len(text):]

##############################################################

#Invoker 
class Editor:
    def __init__(self):
        self.commands= []
        self.undo_stack = []
        self.redo_stack = []

    def add_command(self, command):
        self.commands.append(command)

    def click(self, command):   #run_command
        command.execute()
        self.undo_stack.append(command)

    def go_back(self): #undo_command
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Nothing to undo")

    def go_forward(self): # redo_last
        if self.redo_stack:
            command = self.redo_stack.pop()
            self.click(command)


def client():
    doc = Document()
    editor = Editor()

    add_text_cmd = AddContentCommand(doc, "Hello World")
    cut_text_cmd = CutContentCommand(doc, 5, 11)
    insert_text_cmd = InsertContentCommand(doc,6," Welcome everyone ")

    editor.add_command(add_text_cmd)
    editor.add_command(cut_text_cmd)
    editor.add_command(insert_text_cmd)

    editor.click(add_text_cmd)
    print(doc.content)

    editor.click(cut_text_cmd)
    print(doc.content)
     
    editor.click(insert_text_cmd)
    print(doc.content)

    editor.go_back()
    print(doc.content)

    editor.go_back()
    print(doc.content)
    editor.go_back()
    print(doc.content)

    editor.go_forward()
    print(doc.content)

    add_text_cmd2 = AddContentCommand(doc," Programmers")
    editor.add_command(add_text_cmd2)
    editor.click(add_text_cmd2)
    print(doc.content)

    editor.go_back()
    print(doc.content)

    
    
     
    

client()


         