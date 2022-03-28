def pig_it(text):
    out = []
    for word in text.split(' '):
        if not word.isalpha():
            out.append(word)
            continue
        out.append(word[1:] + word[0] + 'ay')
    return ' '.join(out)


print(pig_it("Hello world    this is me ,..{} / !"))
