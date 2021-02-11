import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().rstrip().split())
inDegree = [0 for i in range(n + 1)]
adjList = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adjList[a].append(b)
    inDegree[b] += 1
stack = [i + 1 for i, v in enumerate(inDegree[1:]) if v == 0]


for _ in range(1, n + 1):
    student = stack.pop()

    for i in adjList[student]:
        inDegree[i] -= 1

        if inDegree[i] == 0:
            stack.append(i)

    print(student, end =' ')


