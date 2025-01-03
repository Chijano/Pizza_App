from Topping import Topping


class Pizza:
    SIZE_PRICES = {
        "Small": 0,   # No additional cost for Small
        "Medium": 50, # Medium adds 50 CZK
        "Large": 100  # Large adds 100 CZK
    }

    def __init__(self, size="Medium"):
        if size not in self.SIZE_PRICES:
            raise ValueError(f"Invalid size. Choose from {list(self.SIZE_PRICES.keys())}")
        self.size = size
        self.description = f"{size} Basic Pizza"
        self.price = 100 + self.SIZE_PRICES[size]

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


def add_topping(topping_name):
    def decorator(pizza_func):
        def wrapper(*args, **kwargs):
            pizza = pizza_func(*args, **kwargs)  # Pass all arguments to the pizza function
            topping_price = Topping.toppings.get(topping_name, 0)
            pizza.description += f", {topping_name}"
            pizza.price += topping_price
            return pizza
        return wrapper
    return decorator


@add_topping("Cheese")
@add_topping("Ham")
def classic_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Salami")
@add_topping("Mushrooms")
def salami_mushroom_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Olives")
@add_topping("Bell Pepper")
@add_topping("Onion")
def vegetarian_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("BBQ Sauce")
@add_topping("Chicken")
@add_topping("Cheese")
def bbq_chicken_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Shrimp")
@add_topping("Mozzarella")
@add_topping("Garlic")
def seafood_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Bacon")
@add_topping("Cheese")
@add_topping("Onion")
def bacon_onion_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Blue Cheese")
@add_topping("Cheese")
@add_topping("Mozzarella")
def four_cheese_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Tuna")
@add_topping("Onion")
def tuna_onion_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Jalapeños")
@add_topping("Salami")
@add_topping("Mozzarella")
def spicy_salami_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Pineapple")
@add_topping("Cheese")
@add_topping("Ham")
def hawaiian_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


recipes = [
    ("Classic Pizza", classic_pizza),
    ("Salami and Mushroom Pizza", salami_mushroom_pizza),
    ("Vegetarian Pizza", vegetarian_pizza),
    ("BBQ Chicken Pizza", bbq_chicken_pizza),
    ("Seafood Pizza", seafood_pizza),
    ("Bacon and Onion Pizza", bacon_onion_pizza),
    ("Four Cheese Pizza", four_cheese_pizza),
    ("Tuna and Onion Pizza", tuna_onion_pizza),
    ("Spicy Salami Pizza", spicy_salami_pizza),
    ("Hawaiian Pizza", hawaiian_pizza),
]