import string
import random

cymbols1 = '$', '@', '!', '%', '#', '*', '&'
cymbols2 = '/', '/', ',', '<', '>', ':', '^', '(', ')', '[', ']', '{', '}'
password_components = ()

print('PASSWORD GENERATOR')
print('The password generator will help you to create hard-to-crack passwords.\nJust fill out the form below and click the Generate button.')

password_length = int(input('Length of the password: '))
# password_components = string.ascii_lowercase + string.ascii_uppercase + string.digits + '[]','{}', '()' + '@', '%', '$'


cymbols_input = input('Include symbols like ($@!%#*&)? Yes or no!').lower()
if cymbols_input == 'yes':
    password_components + cymbols1
else:
cymbols_input2 = ('Include symbols like (/ \ : () [] {} ^ < >)? Yes or no!')

if cymbols_input == 'yes':
    password_components + cymbols2
else:
# lower_case = input('Include lowercase symbols? Yes or no!')
# upper_case = input('Include uppercase? Yes or no!')
# numbers_input = ('Include numbers? Yes or no!')

password = ''.join(random.choice(password_components) for i in range(password_length))
print(password)


# import string
# string.ascii_uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_letters
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
