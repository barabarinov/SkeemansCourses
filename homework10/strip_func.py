def strip(s1, s2):
    s2 = set(s2)

    for i in range(len(s1)):
        if s1[i] not in s2:
            s1 = s1[i:]
            break

    for i in range(len(s1) - 1, -1, -1):
        if s1[i] not in s2:
            s1 = s1[:i + 1]
            break

    return s1

print(strip('HeHlloHe ', 'He'))