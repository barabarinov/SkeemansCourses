from collections import Counter


def duplicate_encode(word):
    out = Counter(word.lower())
    return ''.join(')' if out[i] > 1 else '(' for i in word.lower())


print(duplicate_encode('Success'))  # ")())())"


def duplicate_encode_two(word):
    out = Counter(word.lower())
    same = []
    for i in word.lower():
        if out[i] > 1:
            same.append(')')
        else:
            same.append('(')
    return ''.join(same)


print(duplicate_encode_two('Succes'))
