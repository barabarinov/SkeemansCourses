# FACTORIAL
factorial = 1
counter = int(input('Input a number: '))
for i in range(counter, 0, -1):
    factorial *= i
    i -= 1
    if i == 0:
        print(f"Factorial of {counter} = {factorial}")
