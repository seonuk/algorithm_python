import sys

n = int(sys.stdin.readline().rstrip())
meetingRooms = []
answer = 1

for _ in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    meetingRooms.append((s, e))

meetingRooms.sort(reverse=True)
endTime = meetingRooms.pop()[1]

while meetingRooms:
    nS, nE = meetingRooms.pop()
    if nS >= endTime:
        answer += 1
        endTime = nE

    if nS < endTime and endTime > nE:
        endTime = nE

print(answer)