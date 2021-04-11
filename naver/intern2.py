A = [2, 3, 3, 5, 6, 6]

from sys import setrecursionlimit
setrecursionlimit(4000)
length = len(A) + 1
A.sort(reverse=True)
answer = 0

for i in A:
    length -= 1

    if i == length:
        continue
    else:
        answer += abs(length - i)


print(answer)