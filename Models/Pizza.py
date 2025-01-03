from Topping import Topping


class Pizza:
    def __init__(self):
        self.description = "Basic Pizza"
        self.price = 100

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price


def add_topping(topping_name):
    def decorator(pizza_func):
        def wrapper():
            pizza1 = pizza_func()
            topping_price = Topping.toppings.get(topping_name, 0)
            pizza1.description += f", {topping_name}"
            pizza1.price += topping_price
            return pizza1
        return wrapper
    return decorator


@add_topping("Cheese")
@add_topping("Ham")
def classic_pizza():
    return Pizza()


@add_topping("Salami")
@add_topping("Mushrooms")
def salami_mushroom_pizza():
    return Pizza()


@add_topping("Olives")
@add_topping("Bell Pepper")
@add_topping("Onion")
def vegetarian_pizza():
    return Pizza()


@add_topping("BBQ Sauce")
@add_topping("Chicken")
@add_topping("Cheese")
def bbq_chicken_pizza():
    return Pizza()


@add_topping("Shrimp")
@add_topping("Mozzarella")
@add_topping("Garlic")
def seafood_pizza():
    return Pizza()


@add_topping("Bacon")
@add_topping("Cheese")
@add_topping("Onion")
def bacon_onion_pizza():
    return Pizza()


@add_topping("Blue Cheese")
@add_topping("Parmesan")
@add_topping("Cheese")
@add_topping("Mozzarella")
def four_cheese_pizza():
    return Pizza()


@add_topping("Tuna")
@add_topping("Onion")
def tuna_onion_pizza():
    return Pizza()


@add_topping("Jalapeños")
@add_topping("Salami")
@add_topping("Mozzarella")
def spicy_salami_pizza():
    return Pizza()


@add_topping("Pineapple")
@add_topping("Cheese")
@add_topping("Ham")
def hawaiian_pizza():
    return Pizza()


recipes = [
    ("Hawaiian Pizza", classic_pizza),
    ("Salami and Mushroom Pizza", salami_mushroom_pizza),
    ("Vegetarian Pizza", vegetarian_pizza),
    ("BBQ Chicken Pizza", bbq_chicken_pizza),
    ("Seafood Pizza", seafood_pizza),
    ("Bacon and Onion Pizza", bacon_onion_pizza),
    ("Four Cheese Pizza", four_cheese_pizza),
    ("Tuna and Onion Pizza", tuna_onion_pizza),
    ("Spicy Salami Pizza", spicy_salami_pizza),
    ("Sweet and Savory Pizza", hawaiian_pizza),
]