import sys


N = list(sys.stdin.readline().rstrip())

center = len(N)//2

N = list(map(int, N))
if sum(N[:center]) == sum((N[center:])):
    print("LUCKY")
else:
    print("READY")


# https://www.acmicpc.net/problem/18406