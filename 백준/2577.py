import sys

number = 1
for _ in range(3):
    number *= int(sys.stdin.readline().rstrip())

number = str(number)
for i in range(10):
    print(number.count(str(i)))
