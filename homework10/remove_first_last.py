def remove_char(s):
    return ''.join(s if len(s) <= 3 else s[i] for i in range(1, len(s) - 1))

print(remove_char('Gappaspa'))