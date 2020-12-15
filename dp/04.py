import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

memo = [10001 for _ in range(10001)]
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline().rstrip()))

memo[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        memo[j] = min(memo[j], memo[j - coins[i]] + 1)

if memo[m] == 10001:
    print(-1)
else:
    print(memo[m])