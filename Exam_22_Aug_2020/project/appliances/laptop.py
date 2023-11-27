from project.appliances.appliance import Appliance


class Laptop(Appliance):
    COST = 1

    def __init__(self, cost=COST):
        super().__init__(cost)