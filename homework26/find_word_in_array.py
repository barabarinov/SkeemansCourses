from datetime import datetime

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


def in_array(array1, array2):
    out = set()
    start = datetime.now()
    for i in array1:
        for j in array2:
            if i in j:
                out.add(i)
    print(datetime.now() - start)
    return list(out)


print(in_array(a1, a2))


def find_word_in_array(ar1, ar2):
    out = set()
    start = datetime.now()
    for i in ar1:
        counter = 0
        while counter < len(ar2):
            if i in ar2[counter]:
                out.add(i)
                counter += 1
            else:
                counter += 1
    print(datetime.now() - start)
    return (list(out)).sort()


print(find_word_in_array(a1, a2))
