def is_prime(number):
    if number < 2:
        return number, False

    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return number, False
    return number, True


def get_number_and_check_is_prime():
    number = int(input("Choose your number: "))
    numbers, is_prime_num = is_prime(number)
    if is_prime_num:
        print(f'{numbers} is prime number')
    else:
        print(f'{numbers} is not prime number')


number_of_checks = int(input("Choose your number of checks: "))
for i in range(number_of_checks):
    get_number_and_check_is_prime()
