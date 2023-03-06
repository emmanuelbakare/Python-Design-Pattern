from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def make_payment(self, amount:float) -> str:
        pass 


class CreditCard(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Credit Card")

class DebitCard(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Debit Card")

class Remita(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Remita")

class NetBanking(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using Net Banking")

class PayPal(PaymentMethod):
    def make_payment(self, amount:float) -> str:
        print(f"Pay {amount} using PayPal")

# =============== PAYMENT FACTORY ================ 

class PaymentFactory(ABC):
    def create_payment(self,payment_method):
        pass 

class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, debit_card = DebitCard,paypal = PayPal )
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments[payment_method]()
        
class CanadaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard,paypal = PayPal)
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments[payment_method]()
      
        
class NigeriaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, remita=Remita)
    
    def create_payment(self,payment_method):
        if payment_method in self.payments:
            return self.payments[payment_method]()
         

class Client:
    def __init__(self):
        self.factory = self.get_factory()
        
    

    def get_factory(self):
        factories = dict(us = USPaymentFactory, 
                         nigeria = NigeriaPaymentFactory,
                         canada= CanadaPaymentFactory)
        flist= " ,".join(factories)
        while True:
            factory_type = input(f"Enter Country Payment ({flist}): ")
            if factory_type in factories:
                return factories[factory_type]() 
          
    
    def do_payment(self,amount):
        if self.factory:
            available_payments = ", ".join(self.factory.payments)
            payment_method = input(f" Enter Your Payment Method: ({available_payments}): ")
            if payment_method in self.factory.payments:
                payment= self.factory.payments[payment_method]()
                payment.make_payment(amount)
                
            else:
                 print(f"PAYMENT ERROR: You cannot use this type of payment")
        else:
            print("Payment Class Does Not Exist in our List")

if __name__ == "__main__":
    client=Client()
    amount = input("How Much Are you paying : ")
    client.do_payment(amount)
