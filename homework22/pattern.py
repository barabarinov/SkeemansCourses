def pattern(n):
    out = []
    for i in range(n):
        total = '1'
        for j in range(i):
            total += '*'
        if i > 0:
            total += str(i+1)
        out.append(total)
    return '\n'.join(out)


print(pattern(5))


# 1
# 1*2
# 1**3
# 1***4
# 1****5
