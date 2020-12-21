import sys

n = sys.stdin.readline().rstrip()

result = 0
for i in range(len(n) // 2):
    result += int(n[i])
    result -= int(n[-(i+1)])

if not result:
    print("LUCKY")
else:
    print('READY')