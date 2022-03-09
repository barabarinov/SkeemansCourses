from collections import Counter


def duplicate_count(text):
    return len([v for k, v in (filter(lambda i: i[1] > 1, Counter(text.lower()).items()))])


print(duplicate_count('lolo'))
