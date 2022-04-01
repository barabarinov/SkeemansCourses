MAX_STARS = 30
WIDTH = 80


def print_result(number):
    stars_count = round(MAX_STARS / number)
    if stars_count > MAX_STARS:
        stars_count = MAX_STARS
    number_field_width = WIDTH - 2 * stars_count
    stars  = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'

    print(fmt.format(stars, number))


def div(a, b):
    while True:
        try:
            result = a / b
            print_result(result)
            break
        except (ValueError, ZeroDivisionError) as e:
            print('Error: ', e)
            print('Please try again!')


div(5, 2)
