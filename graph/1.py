import sys

def get_parent(parents, x):
    if parents[x] != x:
        parents[x] = get_parent(parents, parents[x])

    return parents[x]

def union(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)

    if a > b:
        parents[a] = parents[b]
    else:
        parents[b] = parents[a]

def is_same_team(parents, a, b):
    if get_parent(parents, a) == get_parent(parents, b):
        return "YES"
    return "NO"

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parents = [i for i in range(n+1)]

    for _ in range(m):
        funcNum, student1, student2 = map(int, sys.stdin.readline().rstrip().split())

        if funcNum == 0:
            union(parents, student1, student2)

        if funcNum == 1:
            print(is_same_team(parents, student1, student2))