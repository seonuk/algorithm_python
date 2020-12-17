import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

adj = [[] for _ in range(n+1)]
pre = [[] for _ in range(n+1)]

indegree = [0 for _ in range(n+1)]
times = [0 for _ in range(n+1)]

for i in range(1, n+1):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    t, precurri = info[0], info[1:-1]

    times[i] = t

    pre[i] = precurri
    for p in precurri:
        adj[p].append(i)
        indegree[i] += 1

q = deque([i + 1 for i, v in enumerate(indegree[1:]) if v == 0])
nextCurris = []

result = times[:]
while q:
    current = q.popleft()

    for n in adj[current]:
        indegree[n] -= 1
        result[n] = max(result[n], result[current] + times[n])
        if indegree[n] == 0:
            nextCurris.append(n)

    if not q and nextCurris:
        q.extend(nextCurris)
        nextCurris = []

print(result)


# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1