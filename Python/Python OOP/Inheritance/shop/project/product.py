class Product:
    def __init__(self, name: str, quantity: int):
        self.quantity = quantity
        self.name = name

    def decrease(self, quantity: int):
        new_quantity = self.quantity - quantity

        if new_quantity >= 0:
            self.quantity = new_quantity

    def increase(self, quantity: int):
        self.quantity += quantity

    def __repr__(self):
        return self.name
