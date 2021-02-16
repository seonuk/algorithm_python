from sys import stdin

input = stdin.readline

N, M = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
l, partialSum, answer = 0, 0, 0

for r in range(N):
    partialSum += numbers[r]

    while partialSum > M:
        partialSum -= numbers[l]
        l += 1

    if partialSum == M:
        answer += 1

print(answer)