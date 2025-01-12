import tkinter as tk
from View.MainMenu import PizzaAppView

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaAppView(root)
    root.mainloop()