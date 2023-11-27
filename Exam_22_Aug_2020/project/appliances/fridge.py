from project.appliances.appliance import Appliance


class Fridge(Appliance):
    COST = 1.2

    def __init__(self, cost=COST):
        super().__init__(cost)