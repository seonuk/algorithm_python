import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
basket = [i for i in range(n + 1)]

for _ in range(m):
    num1, num2 = map(int, sys.stdin.readline().rstrip().split())

    basket[num1], basket[num2] = basket[num2], basket[num1]

for num in basket[1:]:
    print(num, end=" ")