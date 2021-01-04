import sys

N = int(sys.stdin.readline().rstrip())
coord = []

for _ in range(N):
    pos = tuple(map(int, sys.stdin.readline().rstrip().split()))
    coord.append(pos)

coord.sort(key=lambda x: (x[1], x[0]))

for x,y in coord:
    print(x, y)