import sys

while True:
    pos = list(map(int, sys.stdin.readline().rstrip().split()))
    if not pos:
        break
    else:
        x, y, z = pos[0], pos[1], pos[2]
    print(max(y - x, z - y) - 1)


