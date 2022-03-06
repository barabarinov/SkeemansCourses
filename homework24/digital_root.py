def digital_root(n):
    counter = 0
    while True:
        counter = 0
        for num in str(n):
            counter += int(num)
        if counter < 10:
            return counter
        else:
            n = counter


print(digital_root(493193))


def digital_root_2(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))


print(digital_root_2(999))
