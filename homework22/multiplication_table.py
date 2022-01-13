def multiplication_table(size):
    return [[(x + 1) * (y + 1) for y in range(size)] for x in range(size)]


print(multiplication_table(10))
