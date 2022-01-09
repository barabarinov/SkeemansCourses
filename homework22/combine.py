def combine(a, b):
    merged_dict = {}
    for key in a:
        if key in b:
            new_value = a[key] + b[key]
        else:
            new_value = a[key]

        merged_dict[key] = new_value

    for key in b:
        if key not in merged_dict:
            merged_dict[key] = b[key]

    return merged_dict


objA = { 'a': 10, 'b': 20, 'c': 30 }
objB = { 'a': 3, 'c': 6, 'd': 3 }
objC = { 'a': 5, 'd': 11, 'e': 8 }
objD = { 'c': 3 }
objD = {}, {}, {}
objE = {}
print(combine(objD, objE))
