import sys


N = int(sys.stdin.readline().rstrip())

numbers = []
for _ in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

print(' '.join(map(str,sorted(numbers, key = lambda x: -x))))