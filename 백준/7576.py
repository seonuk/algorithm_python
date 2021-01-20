import sys
from collections import deque


c, r = map(int, sys.stdin.readline().rstrip().split())

tomatoes = []

for _ in range(r):
    tomatoes.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque([])
numbers = 0
count = 0

for i in range(r):
    for j in range(c):
        if tomatoes[i][j] == 1:
            q.append((i, j))
        if tomatoes[i][j] == 0:
            numbers += 1

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]


while q and numbers:
    count += 1
    tmp = []

    while q and numbers:
        n, m = q.popleft()

        for index in range(4):
            nn = n + dn[index]
            nm = m + dm[index]

            if 0 <= nn < r and 0 <= nm < c and tomatoes[nn][nm] == 0:
                tomatoes[nn][nm] = tomatoes[n][m] + 1
                tmp.append((nn, nm))
                numbers -= 1

    q = deque(tmp)

print(count if not numbers else -1)