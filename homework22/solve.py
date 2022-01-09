def solve(arr):
    unique = []
    seen = set()
    for num in reversed(arr):
        if num in seen:
            continue
        else:
            seen.add(num)
            unique.append(num)
    return unique[::-1]


print(solve([1,1,4,5,1,2,1]))
