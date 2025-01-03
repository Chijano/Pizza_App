from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder

    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of {amount} CZK for card {self.card_number}.")


class CashPayment(PaymentStrategy):
    def process_payment(self, amount: float) -> None:
        print(f"Processing cash payment of {amount} CZK.")


class Order:
    def __init__(self):
        self.items = []
        self.total_amount = 0
        self.payment_strategy = None  # No type hint

    def add_item(self, item_name: str, price: float):
        self.items.append((item_name, price))
        self.total_amount += price

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def process_order(self):
        if self.payment_strategy is None:
            print("Payment method not selected.")
            return

        print("\nOrder Summary:")
        for item_name, price in self.items:
            print(f"{item_name}: {price} CZK")
        print(f"Total Amount: {self.total_amount} CZK")
        self.payment_strategy.process_payment(self.total_amount)
