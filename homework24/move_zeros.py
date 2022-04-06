def move_zeros(numbers):
    nums = []
    zeros = []
    for number in numbers:
        if number != 0:
            nums.append(number)
        else:
            zeros.append(number)
    return nums + zeros


print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))


def solve(some_list):
    k = 0
    for i in range(len(some_list)):
        if some_list[i] != 0:
            some_list[k] = some_list[i]
            k+=1
    for j in range(k,len(some_list)):
        some_list[j] = 0
    return some_list


l = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(solve(l))


def lala(n):
    for i in range(n):
        for j in range(i+1):
            print(' ', end=' ')
        for k in range(n-i):
            print('*', end=' ')
        print()


lala(5)
