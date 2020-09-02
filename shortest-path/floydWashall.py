import sys

n = int(sys.stdin.readline())

adj = []

for _ in range(n):
    adj.append(list(map(str, sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] == '1' and adj[k][j] == '1':
                adj[i][j] = '1'

for i in adj:
    print(' '.join(i))