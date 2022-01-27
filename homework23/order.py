def order(string):
    new_dict = {}
    new_list = string.split()
    for word in new_list:
        for letter in word:
            if letter in '123456789':
                new_dict[letter] = word
    return ' '.join(v for k, v in sorted(new_dict.items(), key=lambda x: x[0]))


print(order('is2 Thi1s T4est 3a'))


def order3(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


print(order3('is2 Thi1s T4est 3a'))
