#TWO TRIANGLES
def asterisks(t):
    for i in range(t):
        for j in range(i):
            print(' ', end=' ')
        for k in range(t - i):
            print('*', end=' ')
        print()

    for i in range(t):
        for j in range(t, i + 1, -1):
            print(' ', end=' ')
        for k in range(i + 1):
            print('*', end=' ')
        print()
asterisks(5)