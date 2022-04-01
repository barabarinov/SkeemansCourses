MAX_STARS = 30
WIDTH = 80


def print_result(number):
    if number == 0:
        stars_count = MAX_STARS
    else:
        stars_count = round(MAX_STARS / number)
        if stars_count > MAX_STARS:
            stars_count = MAX_STARS

    number_field_width = WIDTH - 2 * stars_count
    stars  = '*' * stars_count
    fmt = '{0}{1:^' + str(number_field_width) + '}{0}'

    return fmt.format(stars, number)


def div():
    while True:
        try:
            first_number = float(input('Enter first number: '))
            second_number = float(input('Enter second number: '))
            result = first_number / second_number
        except (ValueError, ZeroDivisionError) as e:
            print('Error: ', e)
            print('Please try again!')
        else:
            print(print_result(result))
            break


div()
