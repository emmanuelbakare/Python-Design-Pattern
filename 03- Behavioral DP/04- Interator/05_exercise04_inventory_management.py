from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


# inventory item  (name, quantity )  -- represent individual inventory
class InventoryItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f"Item: {self.name}, Quantity: {self.quantity}"

#inventory iterator 
class InventoryIterator(Iterator):
    def __init__(self, inventory_items):
        self.inventory_items = inventory_items
        self.index = 0

    def has_next(self):
        return self.index < len(self.inventory_items)
    
    def next(self):
        if self.has_next():
            item = self.inventory_items[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

#inventory Management - holds collection of inventory items with method for counting, searching,  and updating
# while iterating throuhg the inventory 
class Inventory:
    def __init__(self):
        self.inventory_items = []
    
    def add_item(self, item):
        self.inventory_items.append(item)

    def create_iterator(self):
        return InventoryIterator(self.inventory_items)

    def count_items(self):
        count = 0
        iterator = self.create_iterator()
        while iterator.has_next():
            item = iterator.next()
            count += item.quantity
        return count

    def search_item(self, name):
        iterator = self.create_iterator()
        while iterator.has_next():
            item = iterator.next()
            if item.name == name:
                return item
        return None

    def update_item_quantity(self, name, new_quantity):
        iterator = self.create_iterator()
        while iterator.has_next():
            item = iterator.next()
            if item.name == name:
                item.update_quantity(new_quantity)
                return True
        return False
    


inventory = Inventory()
inventory.add_item(InventoryItem("Orange", 10))
inventory.add_item(InventoryItem("Milk", 7))
inventory.add_item(InventoryItem("Guava", 15))
inventory.add_item(InventoryItem("Mango", 3))


# Counting items in the inventory
item_count = inventory.count_items()
print("Total item count:", item_count)

# Searching for an item
searched_item = inventory.search_item("Milk")

if searched_item:
    print("Searched item found:", searched_item)
else:
    print("Searched item not found")


# Updating item quantity
updated = inventory.update_item_quantity("Mango", 8)
if updated:
    print("Item quantity updated successfully")
else:
    print("Item not found, quantity not updated")