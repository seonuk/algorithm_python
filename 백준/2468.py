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
    visited = set()
    q = []
    start = []
    count = 0

    for i in range(n):
        for j in range(n):
            if board[i][j] <= w:
                board[i][j] = 0
            else:
                start.append((i, j))

    for (i, j) in start:
        if (i, j) in visited:
            continue

        q = deque([(i, j)])
        count += 1
        visited.add((i, j))

        while q:
            a, b = q.popleft()
            for na, nb in [(a-1, b+0), (a+1, b+0), (a+0, b-1), (a+0, b+1)]:
                if 0 <= na < n and 0 <= nb < n:
                    if (na, nb) not in visited and board[na][nb] != 0:
                        visited.add((na, nb))
                        q.append((na, nb))

    answer = max(answer, count)

print(answer if answer != 0 else 1)

