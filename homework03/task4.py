def even(a):
    if a % 2 == 0:
        print(a, 'Четное')
    else:
        print(a, 'Нечетное')


for i in range(100, -1, -1):
    even(i)
