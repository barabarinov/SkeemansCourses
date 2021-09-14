height = int(input("Input height of triangle: "))
for i in range(height):
    for i in range(i + 1):
        print('*', end=' ')
    print()
for i in range(height, 0, -1):
    for i in range(i, 1, -1):
        print('*', end=' ')
    print()