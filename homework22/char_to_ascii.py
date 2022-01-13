def char_to_ascii(string):
    if string == '':
        return None

    char_dict = {}
    for i in string:
        if i.isalpha():
            char_dict[i] = ord(i)
    return char_dict


print(char_to_ascii('bbbbbqqq'))
