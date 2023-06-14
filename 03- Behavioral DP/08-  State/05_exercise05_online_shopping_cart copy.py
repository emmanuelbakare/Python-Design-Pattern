from abc import ABC, abstractmethod


class ShoppingCartState(ABC):
    @abstractmethod
    def add_item(self, cart, item):
        pass

    @abstractmethod
    def remove_item(self, cart, item):
        pass

    @abstractmethod
    def checkout(self, cart):
        pass

class EmptyState(ShoppingCartState):
    def add_item(self, cart, item):
        print(f"Adding item '{item}' to the cart.")
        cart.items.append(item)
        cart.state = NonEmptyState() 

    def remove_item(self, cart, item):
        print("Cannot remove item. The cart is already empty.") 

    def checkout(self, cart):
        print("Cannot checkout. The cart is empty.")  


class NonEmptyState(ShoppingCartState):
    def add_item(self, cart, item):
        print(f"Adding item '{item}' to the cart.")
        cart.items.append(item)

    def remove_item(self, cart, item):
        if item in cart.items:
            print(f"Removing item '{item}' from the cart.")
            cart.items.remove(item)
            if not cart.items:
                cart.state = EmptyState()

        else:
            print(f"Item '{item}' is not in the cart.")
    
    def checkout(self, cart):
        print("Checking out the cart...")
        # Perform the checkout process
        print("Checkout completed. Thank you!")
        cart.items.clear()
        cart.state = EmptyState()


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.state = EmptyState()

    def add_item(self, item):
        self.state.add_item(self, item) 

    def remove_item(self, item):
        self.state.remove_item(self, item)

    def checkout(self):
        self.state.checkout(self)


# Usage example
cart = ShoppingCart()
cart.add_item("Product 1") 
cart.add_item("Product 2") 
cart.add_item("Product 3") 

cart.remove_item("Product 1")

print()
cart.checkout()

cart.remove_item("Product 2")
cart.checkout()


