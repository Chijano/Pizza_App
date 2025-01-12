from tkinter import Tk, messagebox
from View.MainMenu import MainMenuView
from View.OrderMenu import OrderMenuView
from View.AdminMenu import AdminMenuView
from Models.Order import Order, OrderFactory  # Import the Order class and OrderFactory
from Models.Pizza import (
    classic_pizza, salami_mushroom_pizza, vegetarian_pizza, bbq_chicken_pizza,
    seafood_pizza, bacon_onion_pizza, four_cheese_pizza, tuna_onion_pizza,
    spicy_salami_pizza, hawaiian_pizza
)

class MainController:
    def __init__(self):
        self.root = Tk()
        self.root.title("Pizza Ordering System")

        # Initialize the views
        self.main_menu_view = MainMenuView(self.root, self)  # Pass the controller to the view
        self.order_menu_view = None
        self.admin_menu_view = None

        # Initialize the order object
        self.current_order = Order()  # Now this will work since we imported Order

    def run(self):
        """Start the main event loop."""
        self.main_menu_view.create_main_menu()
        self.root.mainloop()

    def show_order_menu(self):
        """Show the order menu."""
        if self.order_menu_view is None:
            # Pass recipes to the order menu view
            recipes = [
                ("classic", classic_pizza),
                ("salami_mushroom", salami_mushroom_pizza),
                ("vegetarian", vegetarian_pizza),
                ("bbq_chicken", bbq_chicken_pizza),
                ("seafood", seafood_pizza),
                ("bacon_onion", bacon_onion_pizza),
                ("four_cheese", four_cheese_pizza),
                ("tuna_onion", tuna_onion_pizza),
                ("spicy_salami", spicy_salami_pizza),
                ("hawaiian", hawaiian_pizza)
            ]
            self.order_menu_view = OrderMenuView(self.root, self, recipes)  # Pass recipes to the view
        self.main_menu_view.hide_menu()  # Hide the main menu
        self.order_menu_view.create_order_menu()  # Show the order menu

    def find_pizza_function(self, pizza_name):
        """Find the pizza creation function by its name."""
        pizza_func = self.pizza_recipes.get(pizza_name)
        if pizza_func:
            return pizza_func
        else:
            raise ValueError(f"Pizza '{pizza_name}' not found.")

    def add_pizza_to_order(self, pizza_name, size):
        try:
            # Use the OrderFactory to get the correct pizza function based on the pizza name and size
            pizza_func = OrderFactory.get_pizza_function(pizza_name, size)

            if pizza_func:
                # Create the pizza using the function with the selected size
                pizza = pizza_func(size)
                self.current_order.add_pizza(pizza, size)  # Add the pizza to the order, passing the size
            else:
                raise ValueError("Invalid pizza selected")
        except ValueError as e:
            messagebox.showerror("Error", f"Error adding pizza to order: {str(e)}")

    def remove_pizza_from_order(self, pizza_name, size):
        """Remove a pizza from the order."""
        try:
            # Ensure the size is one of the valid options
            valid_sizes = ["small", "medium", "large"]
            size = size.lower().strip()  # Normalize the size input (remove extra spaces and lowercase it)

            if size not in valid_sizes:
                raise ValueError(f"Invalid size: {size}. Valid sizes are: Small, Medium, Large.")

            # Get the pizza creation function from the factory
            pizza_func = OrderFactory.get_pizza_function(pizza_name, size)
            pizza_to_remove = pizza_func()  # This should correctly create the pizza object

            self.current_order.remove_pizza(pizza_to_remove)  # Remove pizza from order
            self.order_menu_view.update_total_price(self.current_order.total_price)  # Update the total price in UI

        except ValueError as e:
            messagebox.showerror("Error", f"Error removing pizza from order: {str(e)}")

    def show_admin_menu(self):
        """Show the admin menu."""
        if self.admin_menu_view is None:
            self.admin_menu_view = AdminMenuView(self.root, self)
        self.main_menu_view.hide_menu()
        self.admin_menu_view.create_admin_menu()

    def show_main_menu(self):
        """Show the main menu again."""
        if self.order_menu_view:
            self.order_menu_view.root.withdraw()  # Properly hide the order menu
        if self.admin_menu_view:
            self.admin_menu_view.root.withdraw()  # Properly hide the admin menu if visible

        self.main_menu_view.root.deiconify()  # Show the main menu window
        self.main_menu_view.create_main_menu()  # Rebuild the main menu
