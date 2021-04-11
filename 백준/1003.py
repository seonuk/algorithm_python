
from sys import stdin

input = stdin.readline

memory = [(1, 0), (0, 1)]

for i in range(2, 41):
    memory.append((memory[i - 1][0] + memory[i - 2][0], memory[i - 1][1] + memory[i - 2][1]))

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    print(memory[n][0], memory[n][1])
