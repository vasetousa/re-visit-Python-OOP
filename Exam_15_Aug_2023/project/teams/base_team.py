from abc import ABC, abstractmethod


class BaseTeam(ABC):
    def __init__(self, name, country, advantage, budget, wins=0):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = wins
        self.equipment = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError('Team name cannot be empty!')
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        value = value.strip()
        if len(value) < 2:
            raise ValueError('Team country should be at least 2 symbols long!')
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError('Advantage must be greater than zero!')
        self.__advantage = value

    @abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        protec = [pr.protection for pr in self.equipment]
        eq_protection = [eq.price for eq in self.equipment]
        if eq_protection:
            total_eq_protection = sum(eq_protection)   # price for all equipment
        else:
            total_eq_protection = 0
        if protec:
            protec_sum = sum(protec)    # all protection sum
            avprotec = protec_sum / len(self.equipment)  # average protection
        else:
            avprotec = 0

        return (
            f'Name: {self.name}\nCountry: {self.country}\nAdvantage: {self.advantage} points\nBudget: {self.budget:.2f}EUR\n'
            f'Wins: {self.wins}\nTotal Equipment Price: {total_eq_protection:.2f}\nAverage Protection: {avprotec:.0f}')