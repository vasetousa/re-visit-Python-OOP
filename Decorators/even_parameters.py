def even_parameters(func):
    def wrapper(*args):
        for a in args:
            end_result = check_if_number(a)
            if not end_result:
                return "Please use only even numbers!"
        return func(*args)

    return wrapper


def check_if_even(data):
    res = data % 2 == 0
    return res


def check_if_number(value):
    if isinstance(value, int):
        result = check_if_even(value)
        return result
    return False


@even_parameters
def add(*args):
    return sum(args)


print(add(2, 4, 6))
print(add(2, 7))
print(add(2, 6, 7))
print(add("Peter", 1))
print(add(2, 6, 12, 90, -20, 34, 44, 50))
