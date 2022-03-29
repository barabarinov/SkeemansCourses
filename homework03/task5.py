# Отделить строки от чисел
# 1
def filtered(y):
    new_list = []
    for i in y:
        if type(i) == str:
            new_list.append(i)
    return new_list


my_list = [1, 3, 'r', 545, 't', 45, 'i', 45, 'great']
print(filtered(my_list))


def filter_list(l):
    return filter(lambda x: not isinstance(x, str), l)


my_list = [2, 434, 64, 'h', 3, 'eyes', 43, 'Pythonloh']
print(filter_list(my_list))


def filter_list(o):
    filter_l = [i for i in o if isinstance(i, str)]
    return filter_l


k = [1, 3, 'r', 45, 'i', 45, 'goat']
print(filter_list(k))


f = [1, 3, 'JekaVolkodav', 45, 'i', 45, 'great']
new_l = [x for x in f if isinstance(x, str)]
print(new_l)
