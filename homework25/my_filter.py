def to_upper(letter: str):
    return letter.upper()


def like_map(func, iterable):
    for i in iterable:
        yield func(i)


for i in like_map(to_upper, ["That's the string", "Hey"]):
    print(i)


def is_even(number: int or float):
    return number % 2 == 1


def like_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


for i in like_filter(is_even, range(12)):
    print(i, end=', ')
