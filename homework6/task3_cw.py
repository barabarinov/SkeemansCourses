#ChristmasTree
# def xmastree(n):
#     counter = 1
#     trunk = n
#     for i in range(n):
#         for j in range(n - 1, 0, -1):
#             print('_', end='')
#         for k in range(i + counter):
#             print('#', end='')
#         counter += 1
#         for l in range(n - 1, 0, -1):
#             print('_', end='')
#         n -= 1
#         print()
#     if trunk < 3:
#         for m in range(0, 1, 1):
#             for o in range(trunk - 1, 0, -1):
#                 print('_', end='')
#             for p in range(1):
#                 print('#', end='')
#             for q in range(trunk - 1, 0, -1):
#                 print('_', end='')
#     else:
#         for r in range(0, 2, 1):
#             for s in range(trunk - 1, 0, -1):
#                 print('_', end='')
#             for t in range(1):
#                 print('#', end='')
#             for u in range(trunk - 1, 0, -1):
#                 print('_', end='')
#             print()
# xmastree(10)
# example
# ____#____
# ___###___
# __#####__
# _#######_
# #########
# ____#____
# ____#____

#VERSION2
def xmastree(n):
    my_list = []
    counter = 1
    trunk = n
    for i in range(n):
        string = ''
        for j in range(n - 1, 0, -1):
            string += '_'
        for k in range(i + counter):
            string += '#'
        counter += 1
        for l in range(n - 1, 0, -1):
            string += '_'
        n -= 1
        my_list.append(string)
    if trunk < 3:
        for m in range(0, 2, 1):
            string = ''
            for o in range(trunk - 1, 0, -1):
                string += '_'
            for p in range(1):
                string += '#'
            for q in range(trunk - 1, 0, -1):
                string += '_'
            my_list.append(string)
    else:
        for r in range(0, 2, 1):
            string = ''
            for s in range(trunk - 1, 0, -1):
                string += '_'
            for t in range(1):
                string += '#'
            for u in range(trunk - 1, 0, -1):
                string += '_'
            my_list.append(string)
    return my_list

for i in xmastree(3):
    print(i)

