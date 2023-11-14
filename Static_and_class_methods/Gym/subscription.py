import data


class Subscription:
    SUBSCRIPTION_ID = data.SUBSCRIPTION_ID

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        Subscription.SUBSCRIPTION_ID += 1

    @staticmethod
    def get_next_id():
        return Subscription.SUBSCRIPTION_ID + 1

    def __repr__(self):
        return f'Subscription <{Subscription.SUBSCRIPTION_ID}> on {self.date}'