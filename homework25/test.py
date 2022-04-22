import string


# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase[13:] + string.ascii_lowercase[:13])


def rot13(s):
    # trans = string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    out = ''
    for letter in s:
        if not letter.isalpha():
            out += letter
        elif letter.isupper():
            out += chr(65 + ord(letter) % 26)
        elif letter.islower():
            out += chr(97 + ord(letter) % 26)
    return out


print(rot13('abcdefghijklmnopqrstuvwxyz'))

for i in 'abcdefghijklmnopqrstuvwxyz':
    print(f'{i} = {ord(i)}')

# A = 65
# B = 66
# C = 67
# D = 68
# E = 69
# F = 70
# G = 71
# H = 72
# I = 73
# J = 74
# K = 75
# L = 76
# M = 77
# N = 78
# O = 79
# P = 80
# Q = 81
# R = 82
# S = 83
# T = 84
# U = 85
# V = 86
# W = 87
# X = 88
# Y = 89
# Z = 90