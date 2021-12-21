import re


def printer_error(s):
    error_values = re.findall(r'[n-z]', s)
    return f'{len(error_values)}/{len(s)}'


print(printer_error("abcdefghijklmnopqrstuvwxyz"))


def printer_error_2(s):
    counter = [i for i in s if i > 'm']
    return f'{len(counter)}/{len(s)}'


print(printer_error_2("abcdefghijklmnopqrstuvwxyz"))
