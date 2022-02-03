def next_bigger(nums):
    if num < 10:
        return None
    else:
        nums = list(str(nums))
        new_list = nums
        for i in reversed(range(len(nums))):
            print(i)
            if nums[i] < nums[i-1]:
                new_list[i], new_list[i-1] = nums[i-1], nums[i]
            if new_list > nums:
                return new_list


a = 12  # 21
b = 513  # 531
c = 2017  # 2071
d = 414  # 441
e = 144  # 414
print(next_bigger(144))


def check(n: int):
    next_big = ''.join(sorted(list(str(n)), reverse=True))
    for i in range(n + 1, int(next_big) + 1):
        if ''.join(sorted(list(str(i)), reverse=True)) == next_big:
            return i
    return -1


print(check(144))
