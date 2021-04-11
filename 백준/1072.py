from sys import stdin
import math

input = stdin.readline

w = 1000000000

x, y = map(int, input().rstrip().split())

z = y/x
z += z + 0.01

a = math.ceil((y-x*z-x) / z)

print(a)