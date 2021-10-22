# def factorial(n):
#     pr = 1
#     for i in range(1, n+1):
#         pr = pr * i
#     print(pr)
#
# factorial(8)

# def multiply(a, b):
#     print(a, b)
#
# def even(a):
#     if a % 2 == 0:
#         print(a, 'Четное')
#     else:
#         print(a, 'Нечетное')

# for i in range(100, -1, -1):
#     even(i)
#
# def example():
#     print(1)
#     print(2)
#     print(3)
#     return 'hello'
#     print(4)
#
# print(example())

# def even(x):
#     if x % 2 == 0:
#         return 'четное'
#     return 'нечетное'
# for i in range(0, 11):
#     print(i,'=', even(i))
#
# def sqAndPer (a, b):
#     mas = []
#     mas.append(a * b)
#     mas.append(2 * (a + b))
#     return mas
# print(sqAndPer(2, 6))
#
# a = (3, 4, 5, 6, 7, 8)
# print(*a)

# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year
# and moreover 50 new inhabitants per year come to live in the town.
# How many years does the town need to see
# its population greater or equal to p = 1200 inhabitants?
#
# 1
def nb_year(p0, percent, aug, p, i=0):
    return i if p0 >= p else nb_year(int(p0 + p0 * (percent / 100) + aug), percent, aug, p, i + 1)


# 2
from itertools import accumulate


def nb_year(p0, pct, aug, p):
    return next(i for i, x in enumerate(accumulate([p0] * 1000, lambda px, _: px + .01 * pct * px + aug)) if x >= p)


# 3
def nb_year(p0, percent, aug, p):
    i = 0
    percent = percent / 100
    while p0 < p:
        p0 += p0 * percent + aug
        i += 1
    return i


l = (1000, 2, 50, 1200)
nb_year(l)

# 4
# def nb_year(p0, percent, aug, p):
#     # your code
#     years = 0
#     per = percent / 100
#     while True:
#         if p0 < p:
#             years += 1
#             p0 = (p0 + (p0 * per) + aug)
#         else:
#             break
#
#     return years
