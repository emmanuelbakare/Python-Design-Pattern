
from abc import ABC, abstractmethod
from typing import List

class ShoppingCart:
    def __init__(self):
        self.items:List['Product'] = []
        self.state:'ShoppingCartState' = EmptyState()

    def add_item(self, item:'Product')-> None:
        self.state.add_item(self, item)

    def remove_item(self, item:'Product')-> None:
        self.state.remove_item(self, item)

    def checkout(self):
        self.state.checkout(self)

class Product:
    def __init__(self,name:str, price:int)-> None: 
        self.name:str = name
        self.price:int = price


class ShoppingCartState(ABC):
    @abstractmethod
    def add_item(self, cart:'ShoppingCart', item:'Product') -> None:
        pass

    @abstractmethod
    def remove_item(self, cart:'ShoppingCart', item:'Product') -> None:
        pass

    @abstractmethod
    def checkout(self, cart:'ShoppingCart') -> None:
        pass

class EmptyState(ShoppingCartState):
    def add_item(self, cart:'ShoppingCart', item:'Product') -> None:
        print(f"Adding  '{item.name}' @ ${item.price} to the cart.")
        cart.items.append(item)
        cart.state = NonEmptyState()

    def remove_item(self, cart:'ShoppingCart', item:'Product')->None:
        print("Cannot remove item. The cart is already empty.")
    
    def checkout(self, cart:'ShoppingCart'):
        print("Cannot checkout. The cart is empty.")


class NonEmptyState(ShoppingCartState):
    def add_item(self, cart:'ShoppingCart', item:'Product') -> None:
        print(f"Adding  '{item.name}' @ ${item.price} to the cart.")
        cart.items.append(item)

    def remove_item(self, cart:'ShoppingCart', item:'Product')->None:
        if item in cart.items:
            print(f"Removing item '{item.name}' from the cart.")
            cart.items.remove(item)
            if not cart.items:
                cart.state = EmptyState()
        else:
            print(f"Item '{item}' is not in the cart.")

    def checkout(self, cart:'ShoppingCart')-> None:
        print("Checking Process...")
        total = 0
        for item in cart.items:
            print("Checking out..", item.name)
            total += item.price
        print(f"Total Price: ${total}")
        print("Checkout completed. Thank you!")
        cart.items.clear()
        cart.state = EmptyState()

# Usage example
cart = ShoppingCart()

item1 = Product("Laptop", 740)
item2 = Product("Printer", 240)
item3 = Product("Scanner", 120)


cart.add_item(item1) 
cart.add_item(item2)  
cart.add_item(item3)  

# cart.remove_item(item2)
print()
cart.checkout() 

# cart.remove_item("Product 2")  #wrong product input
cart.remove_item(item3) 
cart.checkout() 