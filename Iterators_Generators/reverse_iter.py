class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj

    def __iter__(self):
        return reversed(self.iter_obj)


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)





