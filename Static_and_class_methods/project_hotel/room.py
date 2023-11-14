
class Room:
    def __init__(self, number: int, capacity: int, is_taken: bool = False, guests: int = 0):
        self.number = number
        self.capacity = capacity
        self.is_taken = is_taken
        self.guests = guests

    def take_room(self, people):
        if not self.is_taken:
            if self.capacity >= people:
                self.is_taken = True
                self.guests += people
            else:
                return f"Room number {self.number} cannot be taken"
        else:
            return f"Room number {self.number} cannot be taken"
    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0

        else:
            return f'Room number {self.number} is not taken'