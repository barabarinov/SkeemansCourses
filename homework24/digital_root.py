def digital_root(n):
    counter = 0
    while True:
        for num in list(str(n)):
            counter += int(num)
        if len(str(counter)) == 1:
            return counter
        else:
            n = counter
            counter = 0
            continue


print(digital_root(96))
