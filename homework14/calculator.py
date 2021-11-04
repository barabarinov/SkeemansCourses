from operator import sub, add, mul, truediv


def calculate(num1, operation, num2):
    signs = ['-','+', '*', '/']
    if operation not in signs:
        return None
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == '/' and num2 == 0:
        return None
    else:
        return int(num1 / num2)


print(calculate(64, '/', 8))


def calculator(num1, operation, num2):
    mapping = {
        '-': sub,
        '+': add,
        '*': mul,
        '/': truediv,
    }
    if operation not in mapping:
        return None
    try:
        return mapping[operation](num1, num2)
    except ZeroDivisionError:
        return None


print(calculator(3.2, '+', 8))
