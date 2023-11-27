from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    ROOM_COST = 20

    def __init__(self, family_name: str, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two)
        self.room_cost = YoungCouple.ROOM_COST
        self.members_count = 2
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)
