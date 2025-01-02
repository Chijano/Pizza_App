from Pizza import Pizza

class Order:
    order_counter = 1

    def __init__(self):
        self.order_number = Order.order_counter
        Order.order_counter += 1
        self.pizzas = []

    def add_pizza(self, pizza):
        if isinstance(pizza, Pizza):
            self.pizzas.append(pizza)
        else:
            raise ValueError("Only instances of Pizza can be added.")

    def calculate_total(self):
        return sum(pizza.calculate_price() for pizza in self.pizzas)

    def __str__(self):
        pizza_details = "\n".join(str(pizza) for pizza in self.pizzas)
        total = self.calculate_total()
        return f"Order #{self.order_number}:\n{pizza_details}\nTotal: {total} CZK"
    