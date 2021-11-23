# N строки и M столбци
def chessboard(s):
    n, m = map(int, s.split())

    my_list = ''
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                if j % 2 == 0:
                    my_list += '*'
                else:
                    my_list += '.'
            my_list += '\n'
        else:
            for k in range(m):
                if k % 2 == 0:
                    my_list += '.'
                else:
                    my_list += '*'
            my_list += '\n'
    return my_list


col = '10 10'
print(chessboard(col))


def dot_asterisk(b):
    n, m = map(int, b.split())

    my_list = ''
    for i in range(n):
        if i % 2 == 0:
            for j in range(m):
                my_list += ''.join(map('*' if j % 2 == 0 else '.'))
            my_list += '\n'
        else:
            for k in range(m):
                my_list += '.' if k % 2 == 0 else '*'
            my_list += '\n'
    return my_list


print(dot_asterisk('5 3'))
