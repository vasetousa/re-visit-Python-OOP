class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []
        self.member_names = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."