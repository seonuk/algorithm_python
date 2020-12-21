import sys

n = int(sys.stdin.readline().rstrip())

fears = list(map(int, sys.stdin.readline().rstrip().split()))
fears.sort()

count = 0

stack = []
for x in fears:
    stack.append(x)

    if len(stack) >= x:
        count += 1
        stack.clear()

print(count)