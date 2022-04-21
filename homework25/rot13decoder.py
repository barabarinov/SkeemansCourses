import string
from termcolor import colored


def rot13(s):
    chars = string.ascii_uppercase + string.ascii_lowercase
    trans = string.ascii_uppercase[13:] + string.ascii_uppercase[:13] \
            + string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
    out = ''
    for letter in s:
        if not letter.isalpha():
            out += letter
        else:
            out += trans[chars.find(letter)]
    return out


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
