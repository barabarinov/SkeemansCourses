def pig_it(text):
    out = []
    for word in text.split():
        out.append(word[1:] + word[0] + 'ay')
    return ' '.join(out)


print(pig_it('This is my string'))
