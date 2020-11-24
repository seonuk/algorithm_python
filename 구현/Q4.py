import sys

row, column = map(int, sys.stdin.readline().split())

n, m, d = map(int, sys.stdin.readline().split())

board = []

for _ in range(row):
    board.append(list(map(int,sys.stdin.readline().rstrip().split())))


visited = -1
dn = [-1, 0, 1, 0]      #북 동 남 서
dm = [0, 1, 0, -1]

count = 1


while True:
    d = (d - 1) % 4

    for i in range(4):
        nn = n + dn[d]
        nm = m + dm[d]

        if 0 <= nn < column and 0 <= nm < column and board[nn][nm] is 0:
            n = nn
            m = nm

            board[n][m] = visited
            count = count + 1

            break
        else:
            d = (d - 1) % 4
    else:
        d = (d - 2) % 4
        nn = n + dn[d]
        nm = n + dm[d]

        if 0 <= nn < column and 0 <= nm < column and board[nn][nm] is not 1:
            n = nn
            m = nm
        elif board[nn][nm] is 1:
            break

print(count)