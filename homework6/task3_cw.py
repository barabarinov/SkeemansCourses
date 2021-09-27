#ChristmasTree
def xmastree(n):
    counter = 1
    trunk = n
    for i in range(n):
        for j in range(n - 1, 0, -1):
            print('_', end='')
        for k in range(i + counter):
            print('#', end='')
        counter += 1
        for l in range(n - 1, 0, -1):
            print('_', end='')
        n -= 1
        print()
    if trunk < 3:
        for m in range(0, 1, 1):
            for o in range(trunk - 1, 0, -1):
                print('_', end='')
            for p in range(1):
                print('#', end='')
            for q in range(trunk - 1, 0, -1):
                print('_', end='')
    else:
        for r in range(0, 2, 1):
            for s in range(trunk - 1, 0, -1):
                print('_', end='')
            for t in range(1):
                print('#', end='')
            for u in range(trunk - 1, 0, -1):
                print('_', end='')
            print()
xmastree(5)
# example
# ____#____
# ___###___
# __#####__
# _#######_
# #########
# ____#____
# ____#____

