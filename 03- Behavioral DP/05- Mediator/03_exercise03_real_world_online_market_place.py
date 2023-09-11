class OnlineMarketplaceMediator:
    def __init__(self):
        self.sellers = []
        self.buyers = []

    def register_seller(self, seller):
        self.sellers.append(seller)

    def register_buyer(self, buyer):
        self.buyers.append(buyer)

    def notify_sellers(self, buyer, product):
        print()
        for seller in self.sellers:
            seller.receive_message(f"{buyer} is interested in {product}.")

    def notify_buyer(self, seller, product):
        print()
        for buyer in self.buyers:
            buyer.receive_message(f"{seller} has listed {product}.")

class Buyer:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def express_interest(self, product):
        self.mediator.notify_sellers(self.name, product)

    def receive_message(self, message):
        print(f"Buyer {self.name} received message: {message}")

class Seller:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def list_product(self, product):
        self.mediator.notify_buyer(self.name, product)

    def receive_message(self, message):
        print(f"Seller {self.name} received message: {message}")


#client code - Usage
mediator = OnlineMarketplaceMediator()

seller1 = Seller("Seller1", mediator)
seller2 = Seller("Seller2", mediator)


buyer1 = Buyer("Buyer1", mediator)
buyer2 = Buyer("Buyer2", mediator)

mediator.register_seller(seller1)
mediator.register_seller(seller2)

mediator.register_buyer(buyer1)
mediator.register_buyer(buyer2)

seller1.list_product("Product A") 
print()
seller2.list_product("Product B")

print()
buyer1.express_interest("Product B")
print()
buyer2.express_interest("Product A")
