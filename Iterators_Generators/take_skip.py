class take_skip:
    def __init__(self, step: int, count: int):
        self.count = count
        self.step = step

    def __iter__(self):
        self.produced = 0
        return self

    def __next__(self):
        if self.produced < self.count:
            current_produced = self.produced
            self.produced += 1
            return self.step * current_produced
        raise StopIteration


numbers = take_skip(5, 21)
for number in numbers:
    print(number)
