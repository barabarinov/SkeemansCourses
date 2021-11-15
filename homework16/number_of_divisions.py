def divisions(n, divisor):
    counter = 0
    while n >= divisor:
        n /= divisor
        counter += 1
    return counter


print(divisions(3, 3))
