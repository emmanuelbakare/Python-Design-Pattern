from abc import ABC, abstractmethod

class MenuComponent(ABC):
    def __init__(self, name):
        self.name = name 
    
    @abstractmethod
    def display(self):
        pass 

class MenuComposite(MenuComponent):

    @abstractmethod
    def add(self,component):
        pass 

    @abstractmethod
    def remove(self,component):
        pass 



class MenuItem(MenuComponent):
    def __init__(self, name,price ):
        super().__init__(name) 
        self.price  = price
    
    def display(self):
        print(f"{self.name} - ${self.price}")

class MenuItem2(MenuComponent):
    def __init__(self, name, description ):
        super().__init__(name) 
        self.description  = description
    
    def display(self):
        print(f"{self.name} - ({self.description})")

class Menu(MenuComponent):
    def __init__(self, name):
        super().__init__(name)
        self.items = [] 
    
    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def display(self):
        print(f"\n{self.name}\n{'-'*20}")

        for item in self.items:
            item.display() 


main_menu = Menu("Main Menu")

#submenus 
breakfast =  Menu("Breakfast Menu")
lunch = Menu("Lunch Menu")
dinner  = Menu("Dinner Menu")


breakfast.add(MenuItem("Bread Benedict", 8.99))
breakfast.add(MenuItem("Pancake", 6.99))

lunch.add(MenuItem2("Tray","For Putting all the food"))
lunch.add(MenuItem("Burger", 7.99))
lunch.add(MenuItem("Sandwich", 6.99))

dinner.add(MenuItem2("Water","For washing your hand"))
dinner.add(MenuItem("Steak", 19.99))
dinner.add(MenuItem("Salmon", 14.99))

main_menu.add(breakfast)
main_menu.add(lunch)
main_menu.add(dinner)

main_menu.display()

