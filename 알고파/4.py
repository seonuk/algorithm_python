import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

grid = []

for _ in range(n):
    row = list(sys.stdin.readline().rstrip())
    grid.append(row)

dn = [-1, 1, 0, 0]
dm = [0, 0, -1, 1]

save = []
minN = 11
maxN = -1
minM = 11
maxM = -1

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X':
            count = 0

            for k in range(4):
                ni = i + dn[k]
                nj = j + dm[k]

                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == '.':
                        count += 1
                else:
                    count += 1
            if count >= 3:
                save.append((i, j))
            else:
                minN = min(minN, i)
                maxN = max(maxN, i)

                minM = min(minM, j)
                maxM = max(maxM, j)

for i, j in save:
    grid[i][j] = '.'

for i in range(minN, maxN + 1):
    for j in range(minM, maxM + 1):
        print(grid[i][j], end='')
    print()