from itertools import zip_longest


def create_dict(keys, values):
    return dict(zip_longest(keys, values)) if len(keys) > len(values) else dict(zip(keys, values))


a = ['a', 'b', 'c']
b = [1, 2, 3, 4]
print(create_dict(a, b))
