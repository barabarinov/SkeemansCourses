def solve(arr):
    unique = []
    for num in reversed(arr):
        if num in unique:
            continue
        else:
            unique.append(num)
    return list(reversed(unique))


print(solve([1,1,4,5,1,2,1]))  # OK [4,5,2,1] WRONG [1, 2, 4, 5]
