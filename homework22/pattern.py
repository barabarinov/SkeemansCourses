def pattern(n):
    for i in range(n):
        print(1, end='')
        for j in range(i):
            print('*', end='')
        if i > 0:
            print(i+1, end='')
        print()


print(pattern(10))


# 1
# 1*2
# 1**3
# 1***4
# 1****5
# 1*****6
# 1******7
# 1*******8
# 1********9
# 1*********10
