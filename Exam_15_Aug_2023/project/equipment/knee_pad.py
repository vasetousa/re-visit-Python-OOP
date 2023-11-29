from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    def __init__(self, protection: int, price: float):
        super().__init__(protection, price)
        self.price = 15
        self.protection = 120

    def increase_price(self):
        self.price += (15 * 0.2)
        return self.price
