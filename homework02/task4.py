# PALINDROME
word = str(input('Write a word: '))
if word == word[::-1]:
    print(f'"{word}" is a Palindrome!')
else:
    print(f'"{word}" is not a Palindrome!')
