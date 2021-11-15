# N строки и M столбци
def chessboard(s):
    n, m = map(int, s.split())




n = 8
m = 8
list = ''
for i in range(n):
    for j in range(m):
        list += '*.'
    print()

# col = '8 8'
# chessboard(col)
