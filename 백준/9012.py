import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    vps = sys.stdin.readline().rstrip()
    answer = 'NO'
    count = 0

    for i in vps:
        if i == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        answer = 'YES'

    print(answer)