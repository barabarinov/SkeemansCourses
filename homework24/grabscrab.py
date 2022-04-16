from collections import Counter


def grabscrab(example, words):
    out = []
    count_example = Counter(example)
    for word in words:
        if Counter(word) == count_example:
            out.append(word)
    return out


print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))
