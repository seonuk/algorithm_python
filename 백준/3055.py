import sys

r, c = map(int, sys.stdin.readline().rstrip().split())

board = []
target = []
visited = []
f = 0
s = ()

for _ in range(r):
    board.append(list(sys.stdin.readline().rstrip()))
    visited.append([0 for _ in range(c)])

for i in range(r):
    for j in range(c):
        if board[i][j] == 'S':
            s = (i, j, 0)
            visited[i][j] = 1
        if board[i][j] == '*':
            target.append((i, j, 1))
            visited[i][j] = 1

target.append(s)


while target and not f:
    n, m, d = target.pop(0)

    for dn, dm in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nn = n + dn
        nm = m + dm

        if 0 <= nn < r and 0 <= nm < c and board[nn][nm] != 'X' and not visited[nn][nm]:
            if board[nn][nm] == 'D':
                if d: continue
                f = visited[n][m]
                break
            visited[nn][nm] = visited[n][m] + 1
            target.append((nn, nm, d))

print(f if f else 'KAKTUS')