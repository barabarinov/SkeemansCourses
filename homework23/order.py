def order(string):
    new_list = string.split()
    out = [''] * len(new_list)

    for word in new_list:
        for letter in word:
            if letter.isdigit():
                out[int(letter) - 1] = word
                break
    return ' '.join(out)


print(order('is2 Thi1s T4est 3a'))


def order3(words):
    return ' '.join(sorted(words.split(), key=lambda w: sorted(w)))


print(order3('is2 Thi1s T4est 3a'))
