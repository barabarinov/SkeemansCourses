def is_prime_num(number):
    if number < 2:
        return False
    for j in range(2, number // 2 + 1):
        if number % j == 0:
            return False
    return True


def get_number_and_check_is_prime(number):
    for i in range(1, number + 1):
        if i < 2:
            yield i, False
            continue
        yield i, is_prime_num(i)


number = 5
for num, is_prime in get_number_and_check_is_prime(number):
    if is_prime:
        print(f'{num} is prime number')
    else:
        print(f'{num} is not prime number')
