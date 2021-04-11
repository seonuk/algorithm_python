from sys import stdin
from collections import deque

input = stdin.readline

n = int(input().rstrip())
answer = 0
board = []
depth = set()

for _ in range(n):
    row = list(map(int, input().rstrip().split()))

    depth.update(row)
    board.append(row)


for w in sorted(list(depth)):
    visited = [[False for _ in range(n)] for _ in range(n)]
    start = []
    count = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] <= w:
                board[i][j] = 0
                visited[i][j] = True
            else:
                start.append((i, j))

    for (i, j) in start:
        if visited[i][j]:
            continue

        q = deque([(i, j)])
        count += 1
        visited[i][j] = True

        while q:
            a, b = q.popleft()
            for na, nb in [(a-1, b+0), (a+1, b+0), (a+0, b-1), (a+0, b+1)]:
                if 0 <= na < n and 0 <= nb < n:
                    if not visited[na][nb]:
                        visited[na][nb] = True
                        q.append((na, nb))

    answer = max(answer, count)

print(answer if answer != 0 else 1)

