from termcolor import colored


# def rot13(s):
#     out = ''
#     for letter in s:
#         if not letter.isalpha():
#             out += letter
#         elif letter.isupper():
#             out += chr(65 + ord(letter) % 26)
#         elif letter.islower():
#             out += chr(((ord(letter) - 97) + 13) % 26 + 97)
#     return out


def rot13(s):
    return "".join([(chr(((ord(c) - 97) + 13) % 26 + 97) if c.islower() else chr(
        ((ord(c) - 65) + 13) % 26 + 65)) if c.isalpha() else c for c in s])


def main():
    print('This is ' + colored('ROT13 decoder', 'blue'))

    while True:
        print('To quit enter \'q\'')
        text = input('Enter the text to incode/decode ' + colored('> ', 'green'))
        if text != 'q':
            print(rot13(text))
        else:
            break


if __name__ == '__main__':
    main()
