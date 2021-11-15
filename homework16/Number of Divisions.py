def divisions(n, divisor):
    counter = 0
    while True:
        if n < divisor:
            return 0
        n = n / divisor
        counter += 1
        if n < divisor:
            break
    return counter


print(divisions(9, 3))
