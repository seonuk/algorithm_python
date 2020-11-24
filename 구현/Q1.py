import sys

N = int(sys.stdin.readline())
plan = map(str,sys.stdin.readline().split())

direction = {
    'U': 0,
    'D': 1,
    'L': 2,
    'R': 3
}


n = 1
m = 1

dm = [0, 0, -1, 1]  #up down left right
dn = [-1, 1, 0, 0]

for d in plan:
    nn = n + dn[direction[d]]
    nm = m + dm[direction[d]]

    if 1 <= nn <= 5 and 1 <= nm <= 5:
        n = nn
        m = nm

print(n, m)