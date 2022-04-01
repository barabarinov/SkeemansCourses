import warnings

name = input('Enter your first and last name: ')
if name.count(' ') != 1:
    warnings.warn('Name format may be incorrect')

print('Hello, ', name, '!', sep='')
