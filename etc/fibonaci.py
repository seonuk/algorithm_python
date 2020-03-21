#백준 2748번 피보나치

import sys

n = int(sys.stdin.readline())

memory = [0 for i in range(1000)]

def fibo(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    if memory[number] != 0:
        return memory[number]
    else:
        memory[number] = (fibo(number-1) + fibo(number-2))
    return memory[number]


print(fibo(n))