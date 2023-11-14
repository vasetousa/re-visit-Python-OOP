from car import Car


class SportsCar(Car):
    def race(self):
        return 'racing ...'


s = SportsCar()
print(s.race())