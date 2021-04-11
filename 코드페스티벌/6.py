from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().rstrip().split())

store = []
visited = [[-1 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    store.append(list(map(int, input().rstrip().split())))

q = deque([(0, 0)])
visited[0][0] = store[0][0]

while q:
    i, j = q.popleft()

    for ni, nj in [(i + 1, j), (i, j + 1)]:
        if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] < visited[i][j] + store[ni][nj]:
            visited[ni][nj] = visited[i][j] + store[ni][nj]
            q.append((ni, nj))

print(visited[-1][-1])
