import string


def grid(N):
    if N < 0:
        return None
    out = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(string.ascii_lowercase[(i + j) % 26])
        out.append(' '.join(tmp))

    return '\n'.join(out)


print(grid(10))


def grid2(N):
    if N < 0:
        return None

    return '\n'.join(' '.join(string.ascii_lowercase[(i + j) % 26] for i in range(N)) for j in range(N))


print(grid2(12))
