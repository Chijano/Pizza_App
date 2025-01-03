class Sales:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Sales, cls).__new__(cls, *args, **kwargs)
            cls._instance.total_sales = 0
        return cls._instance

    def add_sale(self, amount: float):
        self.total_sales += amount

    def get_total_sales(self) -> float:
        return self.total_sales