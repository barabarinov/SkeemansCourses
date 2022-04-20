from collections import Counter


def grabscrab(word, possible_words):
    out = []
    count_word = Counter(word)
    for wrd in possible_words:
        if Counter(wrd) == count_word:
            out.append(wrd)
    return out


print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))


def find_word(word, possible_words):
    return [wrd for wrd in possible_words if Counter(wrd) == Counter(word)]
