import sys

numbers = list(map(int,sys.stdin.readline().split()))

length = len(numbers)-1         #총 길이에서 -1 만큼 연산시 모두 정렬되기 때문에 -1을

for i in range(length):
    for index,value in enumerate(numbers[:length-i]):
        if value > numbers[index + 1]:
            numbers[index],numbers[index + 1] = numbers[index + 1],numbers[index]

print(numbers)