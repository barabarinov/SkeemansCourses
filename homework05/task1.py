def get_input_and_print(n, m):
    for i in range(n, m + 1):
        print(i, end=' ')


numbers = input("Write two numbers with space: ")
numbers = numbers.split(' ')
try:
    a, b = numbers
    a = int(a)
    b = int(b)
except ValueError as e:
    print(f'ERROR!{e}')
else:
    get_input_and_print(a, b)
