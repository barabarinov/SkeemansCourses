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


def calculate(a, oparation, b):
    mapping = {
        '-': sub,
        '+': add,
        '*': mul,
        '/': divdiv,
        '**': powpow,
    }
    if oparation not in mapping:
        return 'Sign is not correct!'
    try:
        return mapping[oparation](a, b)
    except TypeError as e:
        return 'Error: ', e


print(calculate(0, '**', -30))
