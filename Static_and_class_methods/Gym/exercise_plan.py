import data


class ExercisePlan:
    PLAN_ID = data.PLAN_ID

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        ExercisePlan.PLAN_ID += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        hours = hours * 60  # in minutes
        return cls(trainer_id, equipment_id, hours)

    @staticmethod
    def get_next_id():
        return ExercisePlan.PLAN_ID + 1

    def __repr__(self):
        return f'Plan <{ExercisePlan.PLAN_ID}> with duration {self.duration} minutes'