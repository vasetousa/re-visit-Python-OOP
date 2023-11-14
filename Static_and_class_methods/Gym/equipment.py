import data


class Equipment:
    EQUIPMENT_ID = data.EQUIPMENT_ID

    def __init__(self, name: str):
        self.name = name
        Equipment.EQUIPMENT_ID += 1

    @staticmethod
    def get_next_id():
        return Equipment.EQUIPMENT_ID + 1

    def __repr__(self):
        return f'Equipment <{self.EQUIPMENT_ID}> {self.name}'
