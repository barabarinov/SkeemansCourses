def hi_all():
    one = len([[]])
    two = one + one
    thre = two + one
    four = two + two
    five = two + thre
    seven = four + thre
    eight = four + four
    ten = five + five

    nums = seven * ten + two, \
           ten * ten + one, \
           ten * ten + eight, \
           ten * ten + eight, \
           ten * ten + ten + one, \
           thre * ten + two, \
           eight * ten + seven, \
           ten * ten + ten + one, \
           ten * ten + ten + four, \
           ten * ten + eight, \
           ten * ten,

    return str().join(chr(num) for num in nums)


print(hi_all())
