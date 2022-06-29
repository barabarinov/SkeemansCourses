def find_reverse_number(num):
    counter = 0
    for number in range(100000000):
        if str(number) == str(number)[::-1]:
            counter += 1
        if counter == num:
            return number


print(find_reverse_number(222))


for number in range(100000000):
    print(number)
