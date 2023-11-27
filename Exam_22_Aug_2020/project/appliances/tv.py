from project.appliances.appliance import Appliance


class TV(Appliance):
    COST = 1.5

    def __init__(self, cost=COST):
        super().__init__(cost)