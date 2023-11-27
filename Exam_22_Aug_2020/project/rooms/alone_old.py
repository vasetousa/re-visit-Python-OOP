from project.rooms.room import Room


class AloneOld(Room):
    ROOM_COST = 10
    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension)
        self.room_cost = AloneOld.ROOM_COST
        self.members_count = 1
        self.expenses = self.calculate_expenses()