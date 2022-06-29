from collections import Counter


def grabscrab(said, possible_words):
    return [word for word in possible_words if sorted(word) == sorted(said)]


print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))


def find_word(word, possible_words):
    return [wrd for wrd in possible_words if Counter(wrd) == Counter(word)]


print(find_word("ortsp", ["sport", "parrot", "ports", "matey"]))
