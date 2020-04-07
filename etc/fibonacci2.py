#백준 10038번 피보나치

import sys

n = int(sys.stdin.readline())
answer = [[0, 0] for i in range(n)]

def fibo(number, answer):
    if number == 0:
        answer[0] += 1
        return 0
    if number == 1:
        answer[1] += 1
        return 1
    return fibo(number-1,answer) +fibo(number-2,answer)


for i in range(n):
    _input =int(sys.stdin.readline())
    fibo(_input,answer[i])

for i in range(n):
    print(answer[i][0],answer[i][1])
