class dict_iter:
    def __init__(self, obj):
        self.dict_counter = 0
        self.dict_items = list(obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        counter = self.dict_counter
        if self.dict_counter == len(self.dict_items):
            raise StopIteration

        self.dict_counter += 1
        return f'{self.dict_items[counter]}'


result = dict_iter({1: "1", 2: "2", 3: "3"})
# result = dict_iter({1: "1", 2: "2"})
for x in result:
    print(x)
