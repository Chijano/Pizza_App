import tkinter as tk
from tkinter import messagebox


class MainMenuView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller  # The controller instance passed during initialization
        self.frame = None

    def create_main_menu(self):
        """Create the main menu interface."""
        if self.frame:  # If a menu already exists, destroy it first to avoid duplicating
            self.frame.destroy()

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        tk.Label(self.frame, text="=== Pizza Ordering System ===", font=("Arial", 16)).grid(row=0, column=0,
                                                                                            columnspan=2, pady=10)

        tk.Button(self.frame, text="Create Order", command=self.create_order, width=20).grid(row=1, column=0, pady=5)
        tk.Button(self.frame, text="Payment", command=self.payment, width=20).grid(row=2, column=0, pady=5)
        tk.Button(self.frame, text="Admin Menu", command=self.admin_menu, width=20).grid(row=3, column=0, pady=5)
        tk.Button(self.frame, text="Exit", command=self.exit_application, width=20).grid(row=4, column=0, pady=5)

    def hide_menu(self):
        """Hide the main menu."""
        if self.frame:
            self.frame.pack_forget()  # Remove the menu from the screen

    def create_order(self):
        """Handle creating an order."""
        self.controller.show_order_menu()  # Use controller to show the order menu

    def payment(self):
        """Handle the payment."""
        messagebox.showinfo("Payment", "Payment functionality coming soon.")

    def admin_menu(self):
        """Go to the admin menu."""
        self.controller.show_admin_menu()

    def hide_menu(self):
        """Hide the main menu window."""
        self.root.withdraw()  # Hide the entire window instead of just the frame

    def exit_application(self):
        """Exit the application."""
        self.root.quit()
