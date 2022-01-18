import string


def alphabet_position(text):
    d = {v: str(k) for k, v in enumerate(string.ascii_lowercase, start=1)}
    out = []
    for i in text.lower():
        if i in d:
            out.append(d[i])
    return ' '.join(out)


a = "The sunset sets at twelve o' clock."  # "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
b = "The narwhal bacons at midnight."  # '20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20'

print(alphabet_position(b))
