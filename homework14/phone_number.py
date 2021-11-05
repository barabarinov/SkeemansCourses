def create_phone_number(nums):
    nums = list(map(str, nums))
    return f'({"".join(nums[:3])}) {"".join(nums[3:6])}-{"".join(nums[6:10])}'


n = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(create_phone_number(n))


def create_number(nums):
    nums = list(map(str, nums))
    phone_number = ''.join(i for i in (nums[:3]))
    phone_number = ''.join('(' + phone_number + ') ')
    phone_number += ''.join(j for j in (nums[3:6]))
    phone_number = ''.join(phone_number + '-')
    return phone_number + ''.join(k for k in (nums[6:10]))


n = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(create_number(n))
