def fact(counter):
    factorial = 1
    for i in range(counter, 0, -1):
        factorial *= i
        i -= 1
        if i == 0:
            return f"Factorial of {counter} = {factorial}"


print(fact(7))
