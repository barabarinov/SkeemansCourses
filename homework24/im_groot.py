from collections import Counter
from collections import defaultdict


def count_words_generator(file_lines):
    counted_chars = {}
    for line in file_lines:
        for key, value in Counter(filter(lambda x: x.isalpha(), line.lower())):
            if key not in counted_chars:
                counted_chars[key] = 0
            counted_chars[key] += value
        yield dict(counted_chars)


if __name__ == '__main__':
    with open('/text.txt') as f:
        for counted_words in count_words_generator(f):
            print(counted_words)
