from sys import stdin

input = stdin.readline

n = int(input().rstrip())

s_answer, e_answer = "-1:00", "24:00"

for _ in range(n):
    start, end = map(lambda x: x.strip(), input().rstrip().split('~'))

    if s_answer < start:
        s_answer = start

    if e_answer > end:
        e_answer = end

print(s_answer + " ~" + " " + e_answer if s_answer <= e_answer else -1)