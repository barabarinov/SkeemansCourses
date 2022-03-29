def one_and_zero(arr):
    return int(''.join(str(i) for i in arr), base=2)


print(one_and_zero([1, 1, 1, 1]))


def one_and_zero_vol2(arr):
    accumulate = 0
    for i, value in enumerate(reversed(arr)):
        accumulate += 2 ** i * value
    return accumulate


print(one_and_zero_vol2([0, 1, 1, 0]))
