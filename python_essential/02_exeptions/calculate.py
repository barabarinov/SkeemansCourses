from operator import sub, add, mul


def powpow(a, b):
    try:
        return a ** b
    except ZeroDivisionError as e:
        print('Error: ', e)


def divdiv(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Error: ', e)


def calculate():
    while True:
        expression = input('Enter the expression separeted by spaces: ')
        if expression == 'q':
            break
        else:
            a, operation, b = expression.split()
            a = int(a)
            b = int(b)
            mapping = {
                '-': sub,
                '+': add,
                '*': mul,
                '/': divdiv,
                '**': powpow,
            }
            if operation not in mapping:
                print('Sign is not correct!')
                continue
            try:
                print(f'{"Result: " + str(mapping[operation](a, b)) if mapping[operation](a, b) is not None else ""}')
            except TypeError as e:
                print('Error: ', e)


calculate()
