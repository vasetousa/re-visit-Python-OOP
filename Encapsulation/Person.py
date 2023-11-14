class Person:
    count = 1 # count for first time age setup
    def __init__(self, name, age, pin):
        self.name = name
        self.__age = age
        self.__pin = pin

    @property
    def age(self):
        return f'Age is now {self.__age}'

    @age.setter
    def age(self, value):
        if value < 18 and Person.count == 0:
            print('Age value is under 18 and age will be set to 18')
            self.__age = 18
            Person.count += 1
        elif 0 < value < 18 and Person.count > 0:
            print(f'Age will not be changed!')
        else:
            self.__age = value
            Person.count += 1
            print(f'Age was set to {value}')

    def __name_age(self):
        return f'{self.name} age {self.__age}'

    def info(self, pin_value):
        if self.__pin == pin_value:
            return print(self.__name_age())
        else:
            return print('Wrong pin!')


p = Person('Ivo', 30, 1109)

p.info(1109)
p.age = 10

p.info(1109)
p.age = 20