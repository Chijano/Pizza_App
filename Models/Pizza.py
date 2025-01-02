from Topping import Topping


class Pizza:
    def __init__(self, name, toppings=None):
        self.name = name
        self.toppings = toppings if toppings else []

    def add_topping(self, topping):
        if isinstance(topping, Topping):
            self.toppings.append(topping)
        else:
            raise ValueError("Only instances of Topping can be added.")

    def calculate_price(self):
        return sum(topping.price for topping in self.toppings)

    def __str__(self):
        toppings_list = ", ".join(str(topping.name) for topping in self.toppings)
        return f"Pizza '{self.name}' with toppings: {toppings_list} - Total: {self.calculate_price()} CZK"

    # Predefined pizzas as a class-level dictionary
    basic_pizzas = {
        "Margherita": ["Cheese"],
        "Hawaiian": ["Cheese", "Ham", "Pineapple"],
        "Pepperoni": ["Cheese", "Salami"],
        "Veggie": ["Cheese", "Bell Pepper", "Mushrooms", "Onion", "Olives"],
        "BBQ Chicken": ["Cheese", "Chicken", "Bacon", "Onion", "BBQ Sauce"],
        "Meat Lover's": ["Cheese", "Ham", "Salami", "Bacon"],
        "Four Cheese": ["Cheese", "Mozzarella", "Parmesan", "Blue Cheese"],
        "Seafood": ["Cheese", "Shrimp", "Tuna", "Garlic"],
        "Spicy": ["Cheese", "Salami", "Jalapeños", "Onion"],
        "Supreme": ["Cheese", "Ham", "Salami", "Bell Pepper", "Mushrooms", "Olives"],
    }

    @classmethod
    def create_basic_pizzas(cls):
        pizzas = []
        for name, topping_names in cls.basic_pizzas.items():
            toppings = [Topping(topping, Topping.toppings[topping]) for topping in topping_names]
            pizzas.append(cls(name, toppings))
        return pizzas