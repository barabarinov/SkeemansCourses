def is_isogram(string):
    return len(set(string.lower())) == len(string)


word = "lo" #Dermatoglyphics
if is_isogram(word):
    print(f'\'{word}\' is Isogram')
else:
    print(f'\'{word}\' is not Isogram')
