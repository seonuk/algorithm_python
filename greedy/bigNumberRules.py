import sys

N, M, K = tuple(map(int, sys.stdin.readline().strip().split()))

numbers = list(map(int, sys.stdin.readline().strip().split()))


numbers.sort(key=lambda x: -x)


result = (M // K) * K * numbers[0]+ (M%K)*numbers[1]

print(result)