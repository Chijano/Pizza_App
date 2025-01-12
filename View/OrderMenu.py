import tkinter as tk
from tkinter import messagebox

class OrderMenuView:
    def __init__(self, root, controller, recipes):
        self.controller = controller  # Make sure the controller is passed here
        self.root = root
        self.root.title("Order Menu")

        # Store the recipes passed from the controller
        self.recipes = recipes

        # Pizza selection dropdown
        self.pizza_var = tk.StringVar(value="Choose a pizza")
        self.pizza_menu = tk.OptionMenu(self.root, self.pizza_var, *[recipe[0] for recipe in self.recipes])
        self.pizza_menu.pack(pady=20)

        # Size selection
        self.size_var = tk.StringVar(value="Medium")
        self.size_menu = tk.OptionMenu(self.root, self.size_var, "Small", "Medium", "Large")
        self.size_menu.pack(pady=20)

        # Display selected pizza price
        self.selected_price_label = tk.Label(self.root, text="Price: 100 CZK")  # Default price for basic pizza
        self.selected_price_label.pack(pady=20)

        # Order button
        self.order_button = tk.Button(self.root, text="Add to Order", command=self.add_to_order)
        self.order_button.pack(pady=20)

        # Remove button
        self.remove_button = tk.Button(self.root, text="Remove from Order", command=self.remove_from_order)
        self.remove_button.pack(pady=10)

        # Price display
        self.price_label = tk.Label(self.root, text="Total Price: 0 CZK")
        self.price_label.pack(pady=20)

        # List of pizzas in the current order
        self.order_listbox = tk.Listbox(self.root, width=50, height=10)
        self.order_listbox.pack(pady=20)

        # Bind event to update the price when pizza or size changes
        self.pizza_var.trace("w", self.update_price_display)
        self.size_var.trace("w", self.update_price_display)

    def create_order_menu(self):
        """Method to initialize and display the order menu."""
        self.root.deiconify()  # Show the order menu window

    def update_price_display(self, *args):
        """Update the price display based on selected pizza and size."""
        pizza_name = self.pizza_var.get()
        size = self.size_var.get()

        # Validate pizza selection
        if pizza_name == "Choose a pizza":
            return  # Don't update if no pizza is selected

        # Normalize pizza name to match recipes
        pizza_name = pizza_name.lower()

        # Find the pizza function that corresponds to the selected pizza
        pizza_func = next((recipe[1] for recipe in self.recipes if recipe[0] == pizza_name), None)
        if pizza_func:
            # Ensure pizza_func is callable and instantiate it properly with size
            pizza = pizza_func(size)  # Call the pizza function to create an instance of pizza
            self.selected_price_label.config(text=f"Price: {pizza.get_price()} CZK")
        else:
            self.selected_price_label.config(text="Price: Invalid pizza")

    def update_total_price(self, total_price):
        """Update the total price label in the UI."""
        self.price_label.config(text=f"Total Price: {total_price} CZK")

    def add_to_order(self):
        """Add the selected pizza to the order."""
        pizza_name = self.pizza_var.get()
        size = self.size_var.get()

        # Validate the selection before adding
        if pizza_name == "Choose a pizza":
            messagebox.showerror("Error", "Please select a pizza.")
            return

        try:
            self.controller.add_pizza_to_order(pizza_name, size)  # Add pizza via controller
            pizza_description = f"{pizza_name.capitalize()} ({size.capitalize()})"
            self.order_listbox.insert(tk.END, pizza_description)  # Add the pizza to the listbox
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def remove_from_order(self):
        """Remove the selected pizza from the order listbox and update the controller."""
        selected_index = self.order_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Please select an item to remove.")
            return

        selected_item = self.order_listbox.get(selected_index)
        self.order_listbox.delete(selected_index)

        # Extract pizza name and size from the selected item in the listbox
        pizza_name, size_info = selected_item.split(" (")
        size = size_info.split(")")[0].lower().strip()  # Normalize size (remove spaces, lowercase)

        try:
            self.controller.remove_pizza_from_order(pizza_name.lower(), size)  # Remove pizza via controller
        except ValueError as e:
            messagebox.showerror("Error", str(e))
