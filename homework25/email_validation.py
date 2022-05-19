import re


# . - Any Character Exept new line
# \d - Digit (0-9)
# \D - Not a Digit (0-9)
# \w - Word Character (a-z, A-Z, 0-9, _)
# \W - Not a Word Character
# \s - Whitespace (space, tab, new line)
# \S - Not Whitespace (space, tab, new line)
# \b - Word Boundary
# \B - Not a Word Boundary


# barabarinov@gmail.com
def email_validation(email):
    regex = re.compile(r'([\w\d.\-_]+)@(\w+\.\w+)(\.\w+)?(\.\w+)?')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def main():
    while True:
        email = input('Enter an email> ')
        if email_validation(email):
            print('Email is valid!')
            break
        else:
            print('Email is not valid! Try again!')


if __name__ == __name__:
    main()
