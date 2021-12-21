def double_every_other(lst):
    return [value * 2 if i%2 != 0 else value for i, value in enumerate(lst)]


print(double_every_other([2,3,5,22,211]))
