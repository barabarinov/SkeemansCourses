def move_zeros(numbers):
    nums = []
    zeros = []
    for number in numbers:
        if number != 0:
            nums.append(number)
        else:
            zeros.append(number)
    return nums + zeros


print(move_zeros([0]))
