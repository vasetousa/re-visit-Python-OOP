class Appliance:
    DAYS_EXPENSE = 30

    def __init__(self, cost: float, ): # cost for a day
        self.cost = cost

    def get_monthly_expense(self):
        return self.cost * Appliance.DAYS_EXPENSE