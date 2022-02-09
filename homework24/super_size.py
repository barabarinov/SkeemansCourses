def super_size(n):
    return int(''.join(sorted(str(n), reverse=True)))


print(super_size(419382))
