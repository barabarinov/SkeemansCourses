# Напишите программу-калькулятор, которая поддерживает следующие операции:
# сложение, вычитание, умножение, деление и возведение в степень.
# Программа должна выдавать сообщения об ошибке и продолжать работу
# при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень.
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
            # print(type(a), type(operation), type(b))
            a = int(a)
            operation = str(operation)
            b = int(b)
            # print(type(a), type(operation), type(b))
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
                print(f'Result: {mapping[operation](a, b)}' if not None else '')
            except TypeError as e:
                print('Error: ', e)


print(calculate())
