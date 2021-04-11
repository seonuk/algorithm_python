from sys import stdin
from collections import deque

INF = 987654321
input = stdin.readline

c, r = map(int, input().rstrip().split())
board = []
startingPoint = []
answer = INF

for _ in range(r):
    row = list(input().rstrip())
    board.append(row)

for j, v in enumerate(board[0]):
    if v == 'c':
        startingPoint.append((0, j))


for i, j in startingPoint:
    visited = [[INF for _ in range(c)] for _ in range(r)]

    q = deque([(i, j)])
    visited[i][j] = 0

    while q:
        n, m = q.popleft()

        for nm in [m - 1, m + 1]:
            if 0 <= nm < c and board[n][nm] == '.' and visited[n][nm] > visited[n][m] + 1:
                visited[n][nm] = visited[n][m] + 1
                q.append((n, nm))

        nn = n + 1

        if 0 <= nn < r and board[nn][m] == '.' and visited[nn][m] > visited[n][m]:
            visited[nn][m] = visited[n][m]
            q.append((nn, m))

    answer = min(answer, min((visited[-1])))

print(answer if answer != INF else -1)