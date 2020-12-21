import sys

numbers = sys.stdin.readline().rstrip()
numbers = list(map(int, list(numbers)))
previousNum = numbers[0]
for n in numbers[1:]:
    productResult = previousNum * n
    plusResult = previousNum + n

    if productResult > plusResult:
        previousNum = productResult
    else:
        previousNum = plusResult

print(previousNum)