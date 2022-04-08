from collections import Counter


def groot(contents):
    out1 = {}
    merged_dict = {}
    for phrase in contents:
        if out1 == {}:
            out1 = dict(Counter(phrase.lower()))
            yield out1
            continue
        else:
            out2 = dict(Counter(phrase.lower()))
            for key in out1:
                if key in out2:
                    new_key = out1[key] + out2[key]
                else:
                    new_key = out1[key]

                merged_dict[key] = new_key

            for key in out2:
                if key not in out1:
                    merged_dict[key] = out2[key]
            out1 = merged_dict
        yield out1


with open('/Users/aleksandrbarinov/Downloads/text.txt') as f:
    contents = f.readlines()
for i in groot(contents):
    print(i)
