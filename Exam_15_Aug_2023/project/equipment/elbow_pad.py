from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    def __init__(self, protection: int, price: float):
        super().__init__(protection, price)
        self.price = 25
        self.protection = 90

    def increase_price(self):
        self.price += (25 * 0.1)
        return self.price
