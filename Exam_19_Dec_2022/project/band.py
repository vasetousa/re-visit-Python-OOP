class Band:
    def __init__(self, name: str):
        self.name = name
        self.members = []
        self.member_names = []

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."