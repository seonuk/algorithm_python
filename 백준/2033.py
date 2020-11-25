import sys

N = sys.stdin.readline().strip()
NOD = len(N) - 1

for _ in range(NOD):
    N = str(int(N[:-1]) + bool(int(N[-1]) > 4))

print(int(N) * (10 ** NOD))