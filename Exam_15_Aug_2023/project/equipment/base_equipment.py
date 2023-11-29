from abc import ABC, abstractmethod


class BaseEquipment(ABC):

    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            value = 0
        self.__price = value

    @property
    def protection(self):
        return self.__protection

    @protection.setter
    def protection(self, value):
        if value < 0:
            value = 0
        self.__protection = value

    @abstractmethod
    def increase_price(self):
        pass
