def find_outlier(integers):
    even = []
    odd = []
    for number in integers:
        if number%2:
            odd.append(number)
        else:
            even.append(number)
    if len(even) > len(odd):
        return odd[0]
    else:
        return even[0]


print(find_outlier([2, 4, 3, 6, 8, 10]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, -3, -1719, -19, -11, -13, -21]))


def find_outlier_two(integers):
    assert len(integers) >= 3

    bit = ((integers[0] & 1) +
           (integers[1] & 1) +
           (integers[2] & 1)) >> 1

    for n in integers:
        if (n & 1) ^ bit:
            return n

    assert False


print(find_outlier_two([2, 4, 3, 6, 8, 10]))
print(find_outlier_two([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier_two([160, -3, -1719, -19, -11, -13, -21]))
