def grabscrab(example, words):
    out = []
    for word in words:
        if set(word) == set(example):
            out.append(word)
    return out


print(grabscrab("trisf", ["first"]))
