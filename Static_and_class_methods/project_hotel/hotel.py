
from room import Room


class Hotel:
    def __init__(self, name: str, total_guests: int = 0):
        self.name = name
        self.total_guests = total_guests
        self.rooms = []

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        rm = [rum for rum in self.rooms if rum.number == room_number][0]
        result = rm.take_room(people)
        if result:
            return print(result)
        self.total_guests += rm.guests

    def free_room(self, room_number):
        for rm in self.rooms:
            if rm.number == room_number:
                if rm.is_taken is not False:
                    rm.is_taken = False
                    self.total_guests -= rm.guests
                    rm.guests = 0

    def status(self):
        free_rooms = [frr.number for frr in self.rooms if frr.is_taken == False]
        taken_rooms = [tkr.number for tkr in self.rooms if tkr.is_taken == True]
        result = \
            (f'Hotel {self.name} has {self.total_guests} total guests\nFree rooms: {(', '.join(map(str, free_rooms)))}\n'
            f'Taken rooms: {(', '.join(map(str, taken_rooms)))}')

        return result
