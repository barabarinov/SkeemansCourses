def reverse_words(text):
    out = ''
    total = ''
    for letter in list(text):
        if letter not in ' ':
            out += letter
        else:
            total += ''.join(out[::-1])
            out = ''
            total += ''.join(letter)
    total += ''.join(out[::-1])
    return total


print(reverse_words('double  spaced  words'))


def reverse_words_two(text):
    return ' '.join(s[::-1] for s in text.split(' '))


print(reverse_words_two('a b   c d'))
# PRAY FOR UKRAINE
