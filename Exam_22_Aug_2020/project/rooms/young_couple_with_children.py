from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    ROOM_COST = 30

    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two)
        self.room_cost = YoungCoupleWithChildren.ROOM_COST
        self.members_count = 2 + len(children)
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.children, self.appliances)
