def create_phone_number(nums):
    phone_number = ''
    phone_number = ''.join(str(i) for i in (nums[:3]))
    phone_number = ''.join('(' + phone_number + ') ')
    phone_number += ''.join(str(j) for j in (nums[3:6]))
    phone_number = ''.join(phone_number + '-')
    phone_number += ''.join(str(k) for k in (nums[6:10]))
    return phone_number


n = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(create_phone_number(n))
