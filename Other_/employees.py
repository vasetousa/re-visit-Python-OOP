class Person:
    def __init__(self, name, age, date: str):
        self.date = date
        self.name = name
        self.age = self.set_age(age)

    def set_age(self, age):
        if age <= 0:
            raise ValueError('Age must be a positive number')
        return age


class Employee(Person):
    def __init__(self, name: object, age: object, date: object, origin: object) -> object:
        super().__init__(name, age, date)
        self.origin = origin


class Manager(Person):
    def __init__(self, name, age, date, people_managing):
        super().__init__(name, age, date)
        self.people_managing = people_managing


class Contractor(Person):
    def __init__(self, name, age, date, contract_exp):
        super().__init__(name, age, date)
        self.contract_exp = contract_exp


e = Employee("Ivan", 20, '20-01-2023', 'indian')
c = Contractor("Vason", 50, '22-12-2023', '22-12-2023')
print(e.origin)
print(c.age)
