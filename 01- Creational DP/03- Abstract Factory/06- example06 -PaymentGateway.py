from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def make_payment(self, amount:float)->str:
        pass 

class CreditCard(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        print(f"Pay {amount} using Credit Card") 

class DebitCard(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        print(f"Pay {amount} using Debit Card") 

class Remita(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        print(f"Pay {amount} using Remita") 

class Paypal(PaymentMethod):
    def make_payment(self, amount: float) -> str:
        print(f"Pay {amount} using Paypal") 


# =============== PAYMENT FACTORY ================ 

class PaymentFactory(ABC):
    @abstractmethod
    def create_payment(self, payment_method):
        pass

class USPaymentFactory(PaymentFactory):

    def __init__(self):
        self.payments = dict (
            credit_card = CreditCard,
            debit_card = DebitCard,
            paypal = Paypal
        )

    def create_payment(self, payment_method):
        if payment_method.payment in self.payments:
            return self.payments[payment_method]() 
        
class CanadaPaymentFactory(PaymentFactory):

    def __init__(self):
        self.payments = dict (
            credit_card = CreditCard,
            paypal = Paypal,
            remita = Remita
        )

    def create_payment(self, payment_method):
        if payment_method.payment in self.payments:
            return self.payments[payment_method]() 
        
class NigeriaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict (
            credit_card = CreditCard,
            remita = Remita
        )
    def create_payment(self, payment_method):
        if payment_method.payment in self.payments:
            return self.payments[payment_method]() 


class Client:

    def __init__(self):
        self.factory = self.get_factory()

    def get_factory(self):
        factories = dict(
            us = USPaymentFactory,
            nigeria = NigeriaPaymentFactory,
            canada = CanadaPaymentFactory
        )

        factory_list = " ,".join(factories)

        while True:
            factory_type = input(f"Enter Country Payment ({factory_list}) ")

            if factory_type in factories:
                return factories[factory_type]()
            
    def do_payment(self, amount:float):
        if self.factory:

            available_payment = " ,".join(self.factory.payments)
            payment_method = input(f"Enter Your Payment Method: ({available_payment}) ")

            if payment_method in self.factory.payments:
                payment = self.factory.payments[payment_method]()
                payment.make_payment(amount)
            else:
                print(f"PAYMENT ERROR: You cannot use this type of payment")
        else:
            print("Payment Class Does Not Exist in our List")
            




if __name__ == "__main__":
    client = Client()
    amount = input("Enter The Amount to Pay: ")
    client.do_payment(amount)




