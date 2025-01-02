class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} CZK"

    toppings = {
        "Cheese": 20,
        "Ham": 25,
        "Salami": 30,
        "Mushrooms": 15,
        "Bell Pepper": 10,
        "Olives": 20,
        "Pineapple": 15,
        "Bacon": 35,
        "Onion": 10,
        "Garlic": 5,
    }

    @classmethod
    def get_toppings(cls):
        return [cls(name, price) for name, price in cls.toppings.items()]