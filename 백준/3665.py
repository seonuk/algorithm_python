from sys import stdin
from collections import deque

input = stdin.readline

t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())

    ranks = list(map(int, input().rstrip().split()))
    pointer = [set() for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    for i, v in enumerate(ranks[:-1]):
        tmp = set()

        for node in ranks[i + 1:]:
            tmp.add(node)
            indegree[node] += 1
        else:
            pointer[v] = tmp

    m = int(input().rstrip())
    for _ in range(m):
        a, b = map(int, input().rstrip().split())

        if b in pointer[a]:
            s, e = a, b
        else:
            s, e = b, a

        pointer[s].remove(e)
        pointer[e].add(s)
        indegree[s] += 1
        indegree[e] -= 1

    q = deque([i + 1 for i, v in enumerate(indegree[1:]) if v == 0])
    result = []
    for _ in range(n):
        if len(q) > 1:
            print('?')
            break
        if not q:
            print("IMPOSSIBLE")
            break

        node = q.popleft()

        result.append(node)
        for s in pointer[node]:
            indegree[s] -= 1
            if indegree[s] == 0:
                q.append(s)
    else:
        print(' '.join(map(str, result)))