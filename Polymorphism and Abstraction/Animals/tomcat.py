from cat import Cat


class Tomcat(Cat):
    GENDER = 'male'

    def __init__(self, name: str, age: int):
        super().__init__(name, age, Tomcat.GENDER)

    def make_sound(self):
        return 'Hiss!'
