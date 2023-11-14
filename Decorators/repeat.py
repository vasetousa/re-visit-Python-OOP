def repeat(n):  # ---> use when decorator line 12 has parameter
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(5)  # parameter goes to 'n' from line  1
def say_hi():
    print("Hello")


for a in range(5):
    print('****************')
    say_hi()
print('****************')