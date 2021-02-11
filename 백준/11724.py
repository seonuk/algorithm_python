import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

parents = [i for i in range(n + 1)]
rootNodes = set()

def getRootNode(nodeNum):
    if parents[nodeNum] == nodeNum:
        return nodeNum

    parents[nodeNum] = getRootNode(parents[nodeNum])

    return parents[nodeNum]

def union(a, b):
    aParent = getRootNode(a)
    bParent = getRootNode(b)

    if aParent <= bParent:
        parents[b] = aParent
    else:
        parents[a] = bParent

for _ in range(m):

    u, v = map(int, sys.stdin.readline().rstrip().split())
    union(u, v)

    for i in range(1, n + 1):
        getRootNode(i)

print(len(set(parents)) - 1)

