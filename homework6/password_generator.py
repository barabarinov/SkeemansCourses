import string
import random

# digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
cymbols1 = '/', '/', ',', '<', '>', ':', '^', '(', ')', '[', ']', '{', '}'
cymbols2 = '$', '@', '!', '%', '#', '*', '&'

print('PASSWORD GENERATOR')
print('The password generator will help you to create hard-to-crack passwords.\nJust fill out the form below and click the Generate button.')

password_length = int(input('Length of the password: '))
password_components = string.ascii_lowercase + string.ascii_uppercase + string.digits + cymbols_sum = i for i in range(cymbols1)
password = ''.join(random.choice(password_components) for i in range(password_length))
print(password)

# cymbols_input = input('Include symbols like ($@!%#*&)? Yes or no!')
# if cymbols_input == 'yes'
# cymbols_input2 = ('Include symbols like (/ \ : () [] {} ^ < >)? Yes or no!')
# lower_case = input('Include lowercase symbols? Yes or no!')
# upper_case = input('Include uppercase? Yes or no!')
# numbers_input = ('Include numbers? Yes or no!')

# password_length = random.choice(cymbols1, cymbols_input2, digits, string.ascii_letters)
# print(password)


# import string
# string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
