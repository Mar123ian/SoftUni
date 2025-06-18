from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:


    def __init__(self):
        self.customers=list()
        self.trainers=[]
        self.equipment=[]
        self.plans=[]
        self.subscriptions=[]

    
    def add_customer(self,customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    
    def add_trainer(self,trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    
    def add_equipment(self,equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    
    def add_plan(self,plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    
    def add_subscription(self,subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    
    def subscription_info(self,subscription_id: int):
        subscription=str(next(el if el.id==subscription_id else -1 for el in self.subscriptions))
        customer = str(next(el if el.id == subscription_id else -1 for el in self.customers))
        trainer = str(next(el if el.id == subscription_id else -1 for el in self.trainers))
        equipment = str(next(el if el.id == subscription_id else -1 for el in self.equipment))
        plan = str(next(el if el.id == subscription_id else -1 for el in self.plans))

        output="\n".join([subscription,customer,trainer,equipment,plan])
        return output
