

import abc


class OrderProcessingTemplate(metaclass=abc.ABCMeta):
    def process_order(self, order):
        self.validate_payment(order)
        self.update_inventory(order)
        self.generate_shipping_label(order)
        self.send_order_confirmation(order)

    @abc.abstractmethod
    def validate_payment(self, order):
        pass

    def update_inventory(self, order):
        print("Updating inventory for order:", order)

    @abc.abstractmethod
    def generate_shipping_label(self, order):
        pass

    def send_order_confirmation(self, order):
        print("Sending order confirmation for order:", order)


class CreditCardOrderProcessing(OrderProcessingTemplate): 
    def validate_payment(self, order):
        print("Validating credit card payment for order:", order) 

    def generate_shipping_label(self, order):
        print("Generating shipping label for order:", order)

class PayPalOrderProcessing(OrderProcessingTemplate): 
    def validate_payment(self, order):
        print("Validating PayPal payment for order:", order)

    def generate_shipping_label(self, order):
        print("Generating shipping label for order:", order)



# Usage
if __name__ == "__main__":
    credit_card_order = CreditCardOrderProcessing()
    credit_card_order.process_order("12345") 

    print("-------------------------")

    paypal_order = PayPalOrderProcessing()
    paypal_order.process_order("67890")

    

