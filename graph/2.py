import sys

def get_parents(parents, x):
    if parents[x] != x:
        parents[x] = get_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = get_parents(parents, a)
    b = get_parents(parents, b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


if __name__ == "__main__":

    n, m = map(int, sys.stdin.readline().rstrip().split())

    roads = []
    parents = [i for i in range(n + 1)]
    totalCost = 0
    maxEdgeCost = 0
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())

        roads.append((c, a, b))

    roads.sort()

    for r in roads:
        a = r[1]
        b = r[2]
        c = r[0]

        if get_parents(parents, a) != get_parents(parents, b):
            union_parents(parents, a, b)
            totalCost += c
            maxEdgeCost = c

print(totalCost - maxEdgeCost)