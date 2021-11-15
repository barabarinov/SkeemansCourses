def get_even_numbers(arr):
    return list(filter(lambda x: x % 2 == 0, arr))


print(get_even_numbers([1,2,3,4,5]))
