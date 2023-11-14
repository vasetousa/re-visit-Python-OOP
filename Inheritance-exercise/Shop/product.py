""" Main class """


class Product:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quant: int):
        if quant <= self.quantity:
            self.quantity -= quant

    def increase(self, quant: int):
        self.quantity += quant
