from Pizza import (classic_pizza, salami_mushroom_pizza, vegetarian_pizza, bbq_chicken_pizza, seafood_pizza,
                   bacon_onion_pizza, four_cheese_pizza, tuna_onion_pizza, spicy_salami_pizza, hawaiian_pizza)


class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0

    def add_pizza(self, pizza_func):
        pizza = pizza_func()
        self.pizzas.append(pizza)
        self.total_price += pizza.get_price()

    def display_order(self):
        print("\nYour Order:")
        for index, pizza in enumerate(self.pizzas, 1):
            print(f"{index}. {pizza.get_description()} - {pizza.get_price()} CZK")
        print(f"Total Price: {self.total_price} CZK")


class OrderFactory:
    @staticmethod
    def create_order(pizza_requests):
        order = Order()
        for pizza_type, size in pizza_requests:
            pizza_func = OrderFactory.get_pizza_function(pizza_type, size)
            order.add_pizza(pizza_func)
        return order

    @staticmethod
    def get_pizza_function(pizza_type, size):
        """Retrieves the correct pizza function and injects size."""
        pizza_recipes = {
            "classic": lambda: classic_pizza(size=size),
            "salami_mushroom": lambda: salami_mushroom_pizza(size=size),
            "vegetarian": lambda: vegetarian_pizza(size=size),
            "bbq_chicken": lambda: bbq_chicken_pizza(size=size),
            "seafood": lambda: seafood_pizza(size=size),
            "bacon_onion": lambda: bacon_onion_pizza(size=size),
            "four_cheese": lambda: four_cheese_pizza(size=size),
            "tuna_onion": lambda: tuna_onion_pizza(size=size),
            "spicy_salami": lambda: spicy_salami_pizza(size=size),
            "hawaiian": lambda: hawaiian_pizza(size=size),
        }
        if pizza_type in pizza_recipes:
            return pizza_recipes[pizza_type]
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")
