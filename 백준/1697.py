from sys import stdin
from collections import deque

input = stdin.readline

n, k = map(int, input().rstrip().split())
visited = [False for _ in range(100001)]
visited[n] = True
q = deque([(n, 0)])

while q:
    pos, count = q.popleft()
    if pos == k:
        print(count)
        break

    for i in [2 * pos, pos - 1, pos + 1]:
        if i < 0 or i > 100000 or visited[i]:
            continue

        visited[i] = True
        q.append((i, count + 1))




