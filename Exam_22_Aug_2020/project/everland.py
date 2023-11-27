from project.people.child import Child
from project.rooms.alone_old import AloneOld
from project.rooms.alone_young import AloneYoung
from project.rooms.room import Room
from project.rooms.young_couple import YoungCouple
from project.rooms.young_couple_with_children import YoungCoupleWithChildren


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for rooms in self.rooms:
            # calculation = Room.calculate_expenses(rooms, rooms.children, rooms.appliances)
            if rooms.budget >= rooms.expenses:
                rooms.budget -= rooms.expenses
                result.append(f"{rooms.family_name} paid {rooms.expenses}$ and have {rooms.budget:.2f}$ left.")
            else:
                self.rooms.remove(rooms)
                result.append(f'{rooms.family_name} does not have enough budget and must leave the hotel.')

        return '\n'.join(sorted(result))
    def status(self):
        result = ""

        result += f"Total population: {sum([r.members_count for r in self.rooms])}\n"
        for r in self.rooms:
            result += f"{r.family_name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            if r.children:
                counter = 0
                for c in r.children:
                    counter += 1
                    result += f"--- Child {counter} monthly cost: {(c.cost * 30):.2f}$\n"
            if hasattr(r, 'appliances'):
                total_expenses = 0
                for a in r.appliances:
                    total_expenses += a.get_monthly_expense()
                result += f"--- Appliances monthly cost: {total_expenses:.2f}$\n"

        return result