from sys import stdin

input = stdin.readline

N = int(input())
answer = 0
l, partialSum = 0, 0
primeNumbers = [False, False] + [True for _ in range(2, N + 1)]

for i in range(2, N):
    if primeNumbers[i] == True:
        for j in range(2 * i, N + 1, i):
            primeNumbers[j] = False


primeNumbers = list(i for i, v in enumerate(primeNumbers) if v)


for rNum in primeNumbers:
    partialSum += rNum

    while partialSum > N:
        partialSum -= primeNumbers[l]
        l += 1

    if partialSum == N:
        answer += 1

print(answer)
