def two_sum(nums, target):
    cache = {}
    for i, value in enumerate(nums):
        if value in cache:
            return [cache[value], i]
        cache[target - value] = i


print(two_sum([4, 11, 15, 5], 9))  # [0, 1]
