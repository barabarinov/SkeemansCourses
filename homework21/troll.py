def delete_vowels(string):
    return ''.join(i for i in string if i not in 'AaEeUuOoIi')


print(delete_vowels('This website is for losers LOL!'))
