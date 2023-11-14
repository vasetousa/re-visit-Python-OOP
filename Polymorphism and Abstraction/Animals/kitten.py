from cat import Cat


class Kitten(Cat):
    GENDER = "female"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Kitten.GENDER)

    def make_sound(self):
        return 'Meow!'
