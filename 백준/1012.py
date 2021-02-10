import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    answer = 0

    m, n, k = map(int, sys.stdin.readline().rstrip().split())
    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        board[y][x] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue

            answer += 1
            q = deque([(i, j)])

            while q:
                ci, cj = q.popleft()        # current i, current j

                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni = ci + di
                    nj = cj + dj

                    if 0 <= ni < n and 0 <= nj < m:
                        if board[ni][nj] == 1:
                            board[ni][nj] = 0
                            q.append((ni, nj))

    print(answer)