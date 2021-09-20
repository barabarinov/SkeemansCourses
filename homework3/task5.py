# Отделить строки от чисел
# 1
def filtered(l):
    new_list = []
    for i in l:
        if type(i) == str:
            new_list.append(i)
    return new_list

my_list = [1, 3, 'r', 545, 't', 45, 'i', 45, 'great']
print(filtered(my_list))

# 2???
def filter_list(l):
    return filter(lambda x: not isinstance(x, str), l)

my_list = [2, 434, 64, 'h', 3, 'eyes', 43, 'Pythonloh']
print(filter_list(my_list))

# 3
def filter_list(l):
    filter_list = [i for i in l if isinstance(i, str)]
    return filter_list

l = [1, 3, 'r', 45, 'i', 45, 'goat']
print(filter_list(l))


l = [1, 3, 'JekaVolkodav', 45, 'i', 45, 'great']
new_l = [x for x in l if isinstance(x, str)]
print(new_l)