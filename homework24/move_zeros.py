def move_zeros(numbers):
    zeros = []
    for index, number in enumerate(numbers):
        if number == 0:
            zeros.append(number)
            numbers.pop(index)
    print(numbers)
    print(zeros)
    return numbers.extend(zeros)


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
# print([1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
