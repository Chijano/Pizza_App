import tkinter as tk
from tkinter import messagebox
from Models.Sales import Sales  # Import the Sales class

class AdminMenuView:
    def __init__(self, root):
        self.root = root
        self.sales = Sales()  # Instantiate the Sales singleton
        self.create_admin_menu()

    def create_admin_menu(self):
        self.window = tk.Toplevel(self.root)
        self.window.title("Admin Menu")

        frame = tk.Frame(self.window, padx=20, pady=20)
        frame.pack()

        tk.Label(frame, text="Admin Menu", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons for admin options
        tk.Button(frame, text="View Sales Statistics", command=self.view_sales_statistics).grid(row=1, column=0, pady=10)
        tk.Button(frame, text="Manage Pizzas", command=self.manage_pizzas).grid(row=2, column=0, pady=10)
        tk.Button(frame, text="Back to Main Menu", command=self.window.destroy).grid(row=3, column=0, pady=10)

    def view_sales_statistics(self):
        """Functionality to view sales statistics"""
        total_sales = self.sales.get_total_sales()
        messagebox.showinfo("Sales Statistics", f"Total Sales: {total_sales} CZK")

    def manage_pizzas(self):
        """Functionality to manage pizza menu (e.g., add, remove, update pizzas)"""
        messagebox.showinfo("Manage Pizzas", "Feature coming soon!")