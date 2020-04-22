import sys

numbers = list(map(int,sys.stdin.readline().split()))

for i,v in enumerate(numbers):
    mini = min(numbers[i:])
    m_index = i + numbers[i:].index(mini)
    numbers[i],numbers[m_index] = mini,v

print(numbers)

