import random


def missing_no(nums):
    # counter = 0
    # while True:
    #     if counter in nums:
    #         counter +=1
    #         continue
    #     else:
    #         return counter

    return (set(range(0, 101)) - set(nums)).pop()


numbers = list(range(0, 101))
numbers.remove(100)
random.shuffle(numbers)
print(missing_no(numbers))
