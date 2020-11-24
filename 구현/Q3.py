import sys

position = list(sys.stdin.readline().strip())

dn = [-2, -1, 1, 2, 2, 1, -1, -2]
dm = [1, 2, 2, 1, -1, -2, -2, -1]

count = 0

n, m = (ord(position[0]) - 96), int(position[1])

for i in range(8):
    nn = n + dn[i]
    nm = m + dm[i]

    if 1 <= nn <= 8 and 1 <= nm <= 8:
        count = count + 1

print(count)