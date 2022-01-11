import string


def grid(N):
    new_n = N%len(string.ascii_lowercase)
    print(new_n)
    new_str = ''
    for i in range(N):
        for j in range(N):
            new_str += string.ascii_lowercase[i + j] + ' '
        new_str += '\n'

    return new_str


print(grid(12))


for i in range(5):
    for j in range(i+1):
        print(' ', end=' ')
    for k in range(5 - i):
        print('*', end=' ')
    print()

for i in range(5):
    for j in range(5 - i):
        print(' ', end=' ')
    for k in range(i + 1):
        print('*', end=' ')
    print()


# * * * * *
# * * * *
# * * *
# * *
# *

# *
# * *
# * * *
# * * * *
# * * * * *

# * * * * *
#   * * * *
#     * * *
#       * *
#         *

#         *
#       * *
#     * * *
#   * * * *
# * * * * *
