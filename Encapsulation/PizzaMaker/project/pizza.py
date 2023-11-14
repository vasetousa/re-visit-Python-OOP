from topping import Topping
from dough import Dough


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings: dict = {}

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.__toppings_capacity:
            self.toppings.update({topping.topping_type: topping.weight})
        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        toppings_total_weight = sum(self.toppings.values())
        pizza_dough_weight = self.dough.weight
        total_weight = toppings_total_weight + pizza_dough_weight
        return total_weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, string):
        if not string:
            raise ValueError("The name cannot be an empty string")
        self.__name = string

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, pizza_object: Dough):
        if pizza_object is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = pizza_object

    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, num):
        if not num:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__toppings_capacity = num
