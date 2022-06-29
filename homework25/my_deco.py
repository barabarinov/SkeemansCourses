def my_safe_decorator(func):
    def wrapper(a, b):
        try:
            return func(a, b)
        except:
            return None
    return wrapper


@my_safe_decorator
def some_func(a, b):
    return int(a / b)


print(some_func(4, 0))
print(some_func(4, 4))
print(some_func(4, 2))


def my_safe_decorator(*args):
    def deco(func):
        def wrapper(a, b):
            try:
                return func(a, b)
            except args:
                return None
        return wrapper
    return deco


@my_safe_decorator(ZeroDivisionError, TypeError)
def some_func(a, b):
    return int(a / b)


print(some_func(1, 0))
print(some_func(1, '1'))
print(some_func(4, 2))
