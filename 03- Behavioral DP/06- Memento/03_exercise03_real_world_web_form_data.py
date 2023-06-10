class FormMemento:
    def __init__(self, form_data):
        self.form_data = form_data

    def get_form_data(self):
        return self.form_data 
    
class Form: #originator
    def __init__(self):
        self.data = {} 

    def set_field(self, field_name, field_value):
        self.data[field_name] = field_value 

    def get_field(self, field_name):
        return self.data.get(field_name)
    
    def save_form(self):
        return FormMemento(dict(self.data))
    
    def restore_form_data(self, memento):
        self.data = memento.get_form_data()

    def print_form(self):
        for field_name, field_value in self.data.items():
            print(f"{field_name}: {field_value}")
        print("*"*30)

class Caretaker: #caretaker
    def __init__(self):
        self.mementos = [] 

    def add_mementos(self, memento):
        self.mementos.append(memento)

    def goto_page(self, index):  # get momento
        return self.mementos[index-1]
    

# Usage
form = Form()
caretaker = Caretaker()



# Form page 1

form.set_field("firstname", "Emmanuel")
form.set_field("lastname", "Bakare")
form.set_field("age", 32)
caretaker.add_mementos(form.save_form())
form.print_form()

#Form page 2
form.set_field("Height", 12.5)
form.set_field("document", "classified")
form.set_field("address", "No 4 Allen Avenue, Abuja, Nigeria")
caretaker.add_mementos(form.save_form())
form.print_form()

#Form Page 3
form.set_field("Country", "USA")
form.set_field("color", "black")
form.set_field("class", 10)
caretaker.add_mementos(form.save_form())
form.print_form()

form.restore_form_data(caretaker.goto_page(1))
form.print_form()
