def fizz_buzz(amount):
    my_list = []
    for i in range(1, amount + 1):
        if i%3 == 0 and i%5 == 0:
            my_list.append('fizz buzz')
        elif i%3 == 0:
            my_list.append('Fizz')
        elif i%5 == 0:
            my_list.append('Buzz')
        else:
            my_list.append(str(i))
    return my_list
print(fizz_buzz(45))


def fizz_buzz_gen(amount):
    for i in range(1, amount + 1):
        if i%3 == 0 and i%5 == 0:
            yield 'fizz buzz'
        elif i%3 == 0:
            yield 'Fizz'
        elif i%5 == 0:
            yield 'Buzz'
        else:
            yield i


for i in fizz_buzz_gen(45):
    print(i, end=', ')
