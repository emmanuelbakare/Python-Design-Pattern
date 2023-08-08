'''
Menu
    - MenuItem
    - MenuItem
    - Menu
        - MenuItem
        - MenuItem
'''

class MenuItem:
    def __init__(self, name):
        self.name = name

    def ls(self):
        print(self.name)

class Menu:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
    
    def ls(self):
        print(self.name)
        for item in self.items:
            item.ls() 
    
    
# Create menu items
item1 = MenuItem('item1')
item2 = MenuItem('item2')
item3 = MenuItem('item3')

# Create menus
menu1 = Menu('menu1')
menu2 = Menu('menu2')

menu1.add_item(item1)
menu1.add_item(menu2)
menu2.add_item(item2)
menu2.add_item(item3)

# List items in menus
menu1.ls()
