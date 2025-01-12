from Models.Pizza import (
    classic_pizza, salami_mushroom_pizza, vegetarian_pizza, bbq_chicken_pizza,
    seafood_pizza, bacon_onion_pizza, four_cheese_pizza, tuna_onion_pizza,
    spicy_salami_pizza, hawaiian_pizza
)


class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0

    def add_pizza(self, pizza_name, size):
        """Add a pizza to the order using the pizza name and size."""
        try:
            # Get the pizza creation function based on the pizza name and size
            pizza_func = OrderFactory.get_pizza_function(pizza_name, size)

            if pizza_func:
                pizza = pizza_func(size)  # Call the pizza function with the given size
                self.pizzas.append(pizza)  # Add pizza to the order
                self.total_price += pizza.get_price()  # Update the total price
            else:
                raise ValueError(f"Pizza creation function for '{pizza_name}' not found.")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def remove_pizza(self, pizza):
        """Remove a pizza from the order and adjust the total price."""
        if pizza in self.pizzas:
            self.pizzas.remove(pizza)
            self.total_price -= pizza.get_price()
        else:
            raise ValueError("Pizza not found in order.")

    def display_order(self):
        """Display the current order with prices."""
        print("\nYour Order:")
        for index, pizza in enumerate(self.pizzas, 1):
            print(f"{index}. {pizza.get_description()} - {pizza.get_price()} CZK")
        print(f"Total Price: {self.total_price} CZK")


class OrderFactory:
    pizza_recipes = {
        "classic": classic_pizza,
        "salami_mushroom": salami_mushroom_pizza,
        "vegetarian": vegetarian_pizza,
        "bbq_chicken": bbq_chicken_pizza,
        "seafood": seafood_pizza,
        "bacon_onion": bacon_onion_pizza,
        "four_cheese": four_cheese_pizza,
        "tuna_onion": tuna_onion_pizza,
        "spicy_salami": spicy_salami_pizza,
        "hawaiian": hawaiian_pizza
    }

    @staticmethod
    def get_pizza_function(pizza_name, size):
        """Get the pizza creation function based on the pizza name and size."""
        # Ensure pizza_name is a string and not a Pizza object
        if isinstance(pizza_name, str):
            pizza_func = OrderFactory.pizza_recipes.get(pizza_name)
            if pizza_func:
                return pizza_func  # Return the pizza function if found
            else:
                raise ValueError(f"Pizza '{pizza_name}' not found.")
        else:
            raise ValueError("Invalid pizza name. It must be a string.")
