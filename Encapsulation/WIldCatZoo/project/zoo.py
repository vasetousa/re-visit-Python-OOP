class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.animals_types = []  # added later

    def add_animal(self, animal, animal_price):
        if animal_price <= self.__budget and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= animal_price
            self.animals_types.append(type(animal).__name__)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif len(self.animals) < self.__animal_capacity and animal_price > self.__budget:
            return "Not enough budget"
        return f'Not enough space for {animal.name} the {type(animal).__name__}'

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return f'Not enough space to hire {worker.name} the {type(worker).__name__}'

    def fire_worker(self, worker_name):
        before = len(self.workers)  # number of workers before trying to fire someone. Needed cuz row 27
        [self.workers.remove(w) for w in self.workers if w.name == worker_name]
        after = len(self.workers)
        if before > after:
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = 0
        for sal in self.workers:
            salary_sum += sal.salary
        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You paid your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        if self.__budget >= 155:  # total sum to care for the animals (60 + 50 + 45)
            self.__budget -= 155
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_count = len(self.animals)
        lions = [l for l in self.animals if type(l).__name__ == 'Lion']
        tigers = [t for t in self.animals if type(t).__name__ == "Tiger"]
        cheetahs = [c for c in self.animals if type(c).__name__ == "Cheetah"]

        return (f'You have {animals_count} animals\n----- {len(lions)} Lions: \n{"\n".join(map(str, lions))}\n'
                f'----- {len(tigers)} Tigers: \n{"\n".join(map(str, tigers))}\n'
                f'----- {len(cheetahs)} Cheetahs: \n{"\n".join(map(str, cheetahs))}\n')

    def workers_status(self):
        workers_count = len(self.workers)
        keepers = [k for k in self.workers if type(k).__name__ == 'Keeper']
        caretakers = [c for c in self.workers if type(c).__name__ == "Caretaker"]
        vets = [v for v in self.workers if type(v).__name__ == "Vet"]

        return (f'You have {workers_count} workers\n----- {len(keepers)} Keepers: \n{"\n".join(map(str, keepers))}\n'
                f'----- {len(caretakers)} Caretakers: \n{"\n".join(map(str, caretakers))}\n'
                f'----- {len(vets)} Vets: \n{"\n".join(map(str, vets))}\n')

    def show_types(self):
        types = set(self.animals_types)
        return f'{' *** '.join(types)}'
