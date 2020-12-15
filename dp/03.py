import sys

n = int(sys.stdin.readline().rstrip())

table = [0 for _ in range(10001)]

table[1] = 1
table[2] = 3

for i in range(3, n + 1):
    table[i] = table[i - 2] * 2 + table[i - 1]

print(table[n])