from Food.Project.food import Food


class Fruit(Food):
    def __init__(self, name: str, exp_date: str):
        super().__init__(exp_date)
        self.name = name
