import tkinter as tk
from tkinter import messagebox

class PizzaAppView:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Ordering System")
        self.create_main_menu()

    def create_main_menu(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack()

        # Title label
        tk.Label(frame, text="=== Pizza Ordering System ===", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)

        # Buttons
        tk.Button(frame, text="Create Order", command=self.create_order, width=20).grid(row=1, column=0, pady=5)
        tk.Button(frame, text="Payment", command=self.payment, width=20).grid(row=2, column=0, pady=5)
        tk.Button(frame, text="Admin Menu", command=self.admin_menu, width=20).grid(row=3, column=0, pady=5)
        tk.Button(frame, text="Exit", command=self.exit_application, width=20).grid(row=4, column=0, pady=5)

    def create_order(self):
        messagebox.showinfo("Create Order", "You selected: Create Order")

    def payment(self):
        messagebox.showinfo("Payment", "You selected: Payment")

    def admin_menu(self):
        messagebox.showinfo("Admin Menu", "You selected: Admin Menu")

    def exit_application(self):
        self.root.destroy()