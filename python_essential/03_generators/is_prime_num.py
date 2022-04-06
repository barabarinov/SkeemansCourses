def is_prime_num(number):
    if number < 2:
        yield False

    for j in range(2, number // 2 + 1):
        if number % j == 0:
            yield False
    yield True


def get_number_and_check_is_prime(number):
    for i in range(1, number + 1):
        if i < 2:
            yield False
        for j in range(2, i // 2 + 1):
            if i%j == 0:
                yield i, False
                break
        yield i, True


number = int(input("Choose your number: "))
for num in get_number_and_check_is_prime(number):
    print(num)
    if num:
        print(f'Number is prime')
    else:
        print(f'Number is not prime')
# 1
# 2 Prime
# 3 Prime
# 4 Not Prime
# 5 Prime