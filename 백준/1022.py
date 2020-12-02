import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split())


for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        n = max(abs(i), abs(j))

        distance = abs(n - j) + abs(n - i)
        result = (2*n+1)**2 - distance
        print(result, end=' ')
    print()


