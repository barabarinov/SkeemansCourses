import string


def changer(s):
    out = []
    for letter in (s.lower()):
        if letter in string.ascii_lowercase:
            if letter == 'z':
                out.append(chr(ord('a')).upper())
            else:
                out2 = chr(ord(letter) + 1)
                if out2 in 'aeoui':
                    out.append(out2.upper())
                else:
                    out.append(out2)
        else:
            out.append(letter)
    return ''.join(out)


a = 'Catz30 '  # 'dbUA30'
b = 'sponge1'  # 'tqpOhf1'
c = 'z'  # 'tqpOhf1'
d = 'He llo Wor ld'  # 'If mmp xps mE'
print(changer(a))
