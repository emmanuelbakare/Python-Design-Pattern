
# Element interface
class GUIComponent:
    def accept(self, visitor):
        pass

# Concrete Element: Button
class Button(GUIComponent):
    def accept(self, visitor):
        visitor.visit_button(self)


# Concrete Element: TextField
class TextField(GUIComponent):
    def __init__(self, data=""):
        self.data = data

    def accept(self, visitor):
        visitor.visit_text_field(self)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

# Concrete Element: Label
class Label(GUIComponent):
    def accept(self, visitor):
        visitor.visit_label(self)


# GUI Application class
class GUIApplication:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def process(self, visitor):
        for component in self.components:
            component.accept(visitor)


# Visitor interface
class GUIComponentVisitor:
    def visit_button(self, button):
        pass

    def visit_text_field(self, text_field):
        pass

    def visit_label(self, label):
        pass


# 3 visitors Renderer, EventHandler and DataValidator
# Concrete Visitor: Renderer
class Renderer(GUIComponentVisitor):
    def visit_button(self, button):
        print("Rendering button")

    def visit_text_field(self, text_field):
        print("Rendering text field")

    def visit_label(self, label):
        print("Rendering label")

class EventHandler(GUIComponentVisitor):
    def visit_button(self, button):
        print("Attaching event handler to button")

    def visit_text_field(self, text_field):
        print("Attaching event handler to text field")

    def visit_label(self, label):
        pass

class DataValidator(GUIComponentVisitor):
    def visit_button(self, button):
        pass

    def visit_text_field(self, text_field):
        data = text_field.get_data()
        if data is not None and data != "":
            print("Validating text: ",data)
            print("Validation complete")
        else:
            print("Text field data is empty")

    def visit_label(self, label):
        pass


# Client code
if __name__ == '__main__':
    # Create a GUI application
    app = GUIApplication()

    # Add components to the application
    button = Button()
    text_field = TextField("Hello There")
    label = Label()

    app.add_component(button)
    app.add_component(text_field)
    app.add_component(label)

    # Process the application using visitors
    renderer = Renderer()
    event_handler = EventHandler()
    data_validator = DataValidator()


    app.process(renderer) 
    app.process(event_handler)
    app.process(data_validator)



