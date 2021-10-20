def invert(lst):
    return ([-1 for num in lst])

my_set = ([1, 2, 3, 4, 5])
new_set = ([-1, -2, -3, -4, -5])
shuffle_set = ([0, -1, 2, -3, 4, -5])
print(invert(my_set))
print(invert(new_set))
print(invert(shuffle_set))
# a = 8
# b = a if a > 0 else -a
# print(b)