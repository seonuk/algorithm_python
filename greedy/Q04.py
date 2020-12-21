import sys

n = int(sys.stdin.readline().rstrip())

coins = list(map(int, sys.stdin.readline().rstrip().split()))
coins.sort()

result = 1
for coin in coins:
    if coin > result:
        break

    result += coin
print(result)