def remove_char(s):
    return ''.join(s if len(s) <= 3 else s[i] for i in range(1, len(s) - 1))

print(remove_char('Entrepreneur'))

def remove(s):
    return s[1:len(s) - 1]

print(remove('VVlad is the best prepod!!'))