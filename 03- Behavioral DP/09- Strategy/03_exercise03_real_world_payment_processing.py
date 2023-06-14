# Step 1: Define the Strategy interface
from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Implement the Concrete Strategies
class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card_number, expiry_date, cvv):
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def pay(self, amount):
        print(f"Processing credit card payment of ${amount} with card number {self.card_number}")

class PayPalPaymentStrategy(PaymentStrategy):
    def __init__(self, email, password):
        self.email = email
        self.password = password 

    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount} with email {self.email}")


# Step 3: Create the Context class
class PaymentProcessor:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, amount):
        self.payment_strategy.pay(amount)


# Step 4: Client code
amount = 100

processor = PaymentProcessor(CreditCardPaymentStrategy("1234567890123456", "12/25", "123"))

processor.process_payment(amount)

processor.set_payment_strategy(PayPalPaymentStrategy("example@example.com", "password"))
processor.process_payment(amount)