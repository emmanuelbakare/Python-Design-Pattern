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
        if payment_method in self.payments:
            return self.payments.get(payment_method)() 

class USPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, debit_card = DebitCard,netbanking = NetBanking, paypal = PayPal)

        
class CanadaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, netbanking = NetBanking, paypal = PayPal)

class NigeriaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard, remita=Remita, netbanking = NetBanking)


class IndiaPaymentFactory(PaymentFactory):
    def __init__(self):
        self.payments = dict(credit_card=CreditCard,debit_card = DebitCard, netbanking = NetBanking)

class Client:
    def __init__(self):
        self.factory = None


    def get_factory(self):
        country_factory = dict(us = USPaymentFactory, 
                         nigeria = NigeriaPaymentFactory,
                         canada= CanadaPaymentFactory,
                         india = IndiaPaymentFactory)
        
        flist= " ,".join(country_factory) # us, nigeria, canada
        while not self.factory:
            country = input(f"Enter Country Payment ({flist}): ")

            if country in country_factory:
                self.factory = country_factory.get(country)()
                break
            print(f"You need to enter one of the countries listed ({flist})")

    def do_payment(self):
        if self.factory:
            amount = float(input("How Much Are you paying : "))
            available_payments = ", ".join(self.factory.payments)  #e.g if US = credit_card, debit_card, paypal
            payment_method = input(f"Enter Your Payment Method: ({available_payments}): ")
            if payment_method in self.factory.payments:
                payment= self.factory.payments.get(payment_method)()
                payment.make_payment(amount)
            else:
                 print(f"PAYMENT ERROR: You cannot use this type of payment")
        else:
            print("ERROR: Country Factory Not Properly Created")

    def run_payments(self):
        self.get_factory()
        self.do_payment()


if __name__ == "__main__":
    client=Client()
    client.run_payments()






 
        


