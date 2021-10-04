import string
import random


print('PASSWORD GENERATOR')
print(
    'The password generator will help you to create hard-to-crack passwords.\nJust fill out the form below and click the Generate button.')

def get_password_length():
    while True:
        try:
            password_length = int(input('Length of the password: '))
        except ValueError as e:
            print(f"ERROR {e}")
        else:
            break
    return password_length

def get_selected_symbols():
    password_components = []

    cymbols1 = ['$', '@', '!', '%', '#', '*', '&']
    cymbols2 = ['/', '/', ',', '<', '>', ':', '^', '(', ')', '[', ']', '{', '}']
    cymbols_input = input('Include symbols like ($ @ ! % # * &)? Yes or no! ').lower()
    if cymbols_input == 'yes':
        password_components += cymbols1

    another_cymbols_input2 = input('Include symbols like (/ \ : () [] {} ^ < >)? Yes or no! ').lower()
    if another_cymbols_input2 == 'yes':
        password_components += cymbols2

    lower_case = input('Include lowercase symbols? Yes or no! ').lower()
    if lower_case == 'yes':
        password_components += string.ascii_lowercase

    upper_case = input('Include uppercase? Yes or no! ').lower()
    if upper_case == 'yes':
        password_components += string.ascii_uppercase

    numbers_input = input('Include numbers? Yes or no! ').lower()
    if numbers_input == 'yes':
        password_components += string.digits
    return password_components

def get_password(selected_symbols, password_length):
    password = ''.join(random.choice(selected_symbols) for i in range(password_length))
    return (f'Your password is {password}')

def main():
    return (get_password(get_selected_symbols(), get_password_length()))
    print(get_password())

if __name__ == '__main__':
    main()