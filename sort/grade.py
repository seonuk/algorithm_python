import sys

N = int(sys.stdin.readline().rstrip())

gradeInfos = []

for _ in range(N):
    gradeInfos.append(tuple(sys.stdin.readline().rstrip().split()))


gradeInfos.sort(key= lambda x : x[1])

for grade in gradeInfos:
    print(grade[0], end = ' ' )
