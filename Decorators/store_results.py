class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open('results.txt', 'a+') as the_file:
            result = self.func(*args)
            the_file.writelines(f'Function "{self.func.__name__}" was called. Result: {result} \n')


class read_results:
    def __init__(self, func):
        self.func = func
        self.lines = []

    def __call__(self, *args):
        with open('results.txt', 'r+') as the_file:
            result = the_file.readline()
            self.lines.append(result)
            return print(result)


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


@read_results
def read(func):
    return


# add(2, 2)
# mult(6, 4)

read()