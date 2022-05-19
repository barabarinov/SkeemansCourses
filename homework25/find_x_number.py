def find_x_number(number):
    ...


print(find_x_number('x + 1 = 9 - 2'))
# 6


def task(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()


task(3)
