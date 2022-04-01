# Напишите программу-калькулятор, которая поддерживает следующие операции:
# сложение, вычитание, умножение, деление и возведение в степень.
# Программа должна выдавать сообщения об ошибке и продолжать работу
# при вводе некорректных данных, делении на ноль и возведении нуля в отрицательную степень.
from operator import sub, add, mul, truediv, pow


def calc(a, oparation, b):
    mapping = {
        '-': sub,
        '+': add,
        '*': mul,
        '/': truediv,
        '**': pow,
    }
    if oparation not in mapping:
        return 'Sign is not correct!'
    try:
        return mapping[oparation](a, b)
    except (ZeroDivisionError, TypeError) as e:
        print('Error', e)


print(calc(0, '**', 10))
