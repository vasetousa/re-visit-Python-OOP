import data
from Static_and_class_methods.Gym.customer import Customer
from Static_and_class_methods.Gym.equipment import Equipment
from Static_and_class_methods.Gym.subscription import Subscription
from Static_and_class_methods.Gym.trainer import Trainer
from Static_and_class_methods.Gym.exercise_plan import ExercisePlan


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        current_subscription = [su for su in self.subscriptions if su.SUBSCRIPTION_ID == subscription_id]
        if current_subscription:
            current_subscription = current_subscription[0]
            current_customer = [c for c in self.customers if c.CUSTOMER_ID == current_subscription.customer_id][0]
            current_trainer = [t for t in self.trainers if t.TRAINER_ID == current_subscription.trainer_id][0]
            current_plan = [p for p in self.plans if p.PLAN_ID == current_subscription.exercise_id][0]
            current_equipment = [e for e in self.equipment if e.EQUIPMENT_ID == current_plan.equipment_id][0]
            return f'{current_subscription}\n{current_customer}\n{current_trainer}\n{current_equipment}\n{current_plan}'




