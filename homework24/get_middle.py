def get_middle(s):
    if not s:
        return ''
    return s[(len(s) // 2) - 1: len(s) // 2 + 1] if len(s)%2 == 0 else s[len(s) // 2]


print(get_middle('n'))


def get_middle_2(s):
    if not s:
        return ''
    if len(s)%2 == 0:
        print((len(s) // 2) - 1)
        print(len(s) // 2 + 1)
        return s[(len(s) // 2) - 1: len(s) // 2 + 1]
    else:
        print(s[0])
        return s[len(s) // 2]


print(get_middle_2('nm'))
