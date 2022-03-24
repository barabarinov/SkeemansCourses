def find_missing_letter(chars):
    for i, j in zip(chars, chars[1:]):
        if ord(j) != ord(i)+1:
            return chr(ord(i) + 1)
    raise ValueError('Expected list with one missing character!')


print(find_missing_letter(['a', 'c']))
