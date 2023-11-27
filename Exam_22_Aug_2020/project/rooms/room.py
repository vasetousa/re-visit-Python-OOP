from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:
    ROOM_COST = 30
    def __init__(self, family_name: str, budget: float):
        self.family_name = family_name
        self.budget = budget
        self.members_count = 0
        self.children = []
        self.room_cost = Room.ROOM_COST
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value

    def calculate_expenses(self, *data):
        total_expenses = 0
        for el in data:
            for el in el:
                if isinstance(el, Appliance):
                    total_expenses += el.get_monthly_expense()
                elif isinstance(el, Child):
                    total_expenses += el.cost * 30
        self.expenses = total_expenses + self.room_cost
        return self.expenses   # children + appliances + room