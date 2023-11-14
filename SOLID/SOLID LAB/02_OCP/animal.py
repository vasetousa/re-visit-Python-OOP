class Animal:
    def __init__(self, species, sound):
        self.sound = sound
        self.species = species
        self.data = {species: sound}

    def get_species(self):
        return self.species

    def animal_sound(self, species):
        return f"{self.data[species]}"


# animals = [Animal('cat'), Animal('dog')]
animals = [Animal('cat', 'meow'), Animal('dog', 'woof-woof'), Animal('chicken', 'cluck')]
animals2 = [Animal('cat', 'meow'), Animal('dog', 'woof-woof'), Animal('chicken', 'cluck'), Animal('cow', 'moo')]

for a in animals2:
    sp = a.get_species()
    print(a.animal_sound(sp))

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
