def char_to_ascii(string):
    char_dict = {}
    some_set = set()
    for i in string:
        if i in '':
            return None
        if i in some_set:
            continue
        char_dict[i] = ord(i)
        some_set.add(i)
        return char_dict


print(char_to_ascii('bbbbbqqq'))

# char_dict[ord(i)] for i in string if i in some_set continue
