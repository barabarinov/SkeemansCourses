def wave_sort(a):
    for i in range(len(a) - 1):
        if i%2 == 0:
            if a[i] > a[i+1]:
                continue
            else:
                a[i], a[i+1] = a[i + 1], a[i]
                continue
        if a[i] < a[i+1]:
            continue
        else:
            a[i], a[i + 1] = a[i + 1], a[i]
    return a


a = [1, 10, 5, 7, 2, 6]
b = [1, 57, 43, 50, 7, 90]
print(wave_sort(a))
