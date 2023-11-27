from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    ROOM_COST = 10
    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary)
        self.room_cost = AloneYoung.ROOM_COST
        self.members_count = 1
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)
