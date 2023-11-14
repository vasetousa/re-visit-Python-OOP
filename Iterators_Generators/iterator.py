

class custom_range:
    def __init__(self, start, end):
        self.end = end
        self.start = start

    def __iter__(self):
        return self.Iterator(self)

    class Iterator:
        def __init__(self, custom_range_obj):
            self.custom_range_obj = custom_range_obj
            self.data = custom_range_obj.start

        def __iter__(self):
            return self

        def __next__(self):
            if self.custom_range_obj.end < self.data:
                raise StopIteration
            data = self.data
            self.data += 1
            return data




cr = custom_range(1, 10)
# iter1 = iter(cr)
# iter2 = iter(cr)
for x in cr:    # iter1
    print(x)
