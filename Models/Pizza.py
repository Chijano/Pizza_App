from Models.Topping import Topping  # Import the Topping class

class Pizza:
    SIZE_PRICES = {
        "Small": 0,
        "Medium": 50,
        "Large": 100
    }

    def __init__(self, size="Medium"):
        self.set_size(size)

    def set_size(self, size):
        """Sets the size and updates the price."""
        if size not in self.SIZE_PRICES:
            raise ValueError(f"Invalid size. Choose from {list(self.SIZE_PRICES.keys())}")
        self.size = size
        self.description = f"{size} Basic Pizza"
        self.price = 100 + self.SIZE_PRICES[size]

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def __eq__(self, other):
        """Compare two pizza objects based on size, description, and price."""
        if isinstance(other, Pizza):
            return self.description == other.description and self.size == other.size
        return False


def add_topping(topping_name):
    """Decorator function to add a topping to a pizza."""
    def decorator(pizza_func):
        def wrapper(*args, **kwargs):
            pizza = pizza_func(*args, **kwargs)  # Call the pizza creation function
            topping_price = Topping.toppings.get(topping_name, 0)
            pizza.description += f", {topping_name}"
            pizza.price += topping_price
            return pizza
        return wrapper
    return decorator


# Define pizza recipes with toppings using decorators
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


@add_topping("Spicy Salami")
@add_topping("Jalapenos")
def spicy_salami_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza


@add_topping("Pineapple")
@add_topping("Ham")
def hawaiian_pizza(size="Medium"):
    pizza = Pizza(size=size)
    return pizza
