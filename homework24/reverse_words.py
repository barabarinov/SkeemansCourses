def reverse_words(text):
    print(list(text))
    return ''.join(word[::-1] for word in list(text))


print(reverse_words('Albina Bethel Circa Den Enemy'))
