class Child:
    def __init__(self, food_cost: int, *toy_cost):
        self.toy_cost = toy_cost
        self.food_cost = food_cost
        self.cost = sum([t for t in self.toy_cost]) + food_cost
        self.a = 1
