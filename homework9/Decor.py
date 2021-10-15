def add_some_number(arg):
    def some_func(func):
        def wrapper(*args, **kwargs):
                result = func(*args, **kwargs)
                result += arg
                return result
        return wrapper
    return some_func

@add_some_number(12)
def sum(a, b):
    return a + b

@add_some_number(8)
def sub(a, b):
    return a - b

a = sum(2, 4)
print(f'result is {a}')

b = sub(10, 7)
print(f'result is {b}')
