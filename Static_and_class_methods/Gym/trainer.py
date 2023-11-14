import data


class Trainer:
    TRAINER_ID = data.TRAINER_ID

    def __init__(self, name: str):
        self.name = name
        Trainer.TRAINER_ID += 1

    @staticmethod
    def get_next_id():
        return Trainer.TRAINER_ID + 1

    def __repr__(self):
        return f'Trainer <{Trainer.TRAINER_ID}> {self.name}'