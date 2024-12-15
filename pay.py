from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid {amount} using PayPal")

class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card")

class PaymentContext:
    def __init__(self, strategy: Payment):
        self._strategy = strategy

    def set_payment(self, strategy: Payment):
        self._strategy = strategy

    def execute_payment(self, amount: float):
        self._strategy.pay(amount)
