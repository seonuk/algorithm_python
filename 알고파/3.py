import sys

d = {
    "R": 0,
    "L": 1,
    "B": 2,
    "T": 3,
    "RT": 4,
    "LT": 5,
    "RB": 6,
    "LB": 7
}


dn = [0, 0, -1, 1, 1, 1, -1, -1]
dm = [1, -1, 0, 0, 1, -1, 1, -1]

king_pos, stone_pos, times = map(str, sys.stdin.readline().rstrip().split())

king_pos = list(king_pos)
king_pos[0] = ord(king_pos[0])      #m
king_pos[1] = int(king_pos[1])      #n

stone_pos = list(stone_pos)
stone_pos[0] = ord(stone_pos[0])    #m
stone_pos[1] = int(stone_pos[1])    #n

for _ in range(int(times)):
    move = sys.stdin.readline().rstrip()

    king_nn = king_pos[1] + dn[d[move]]
    king_nm = king_pos[0] + dm[d[move]]


    if king_nn == stone_pos[1] and king_nm == stone_pos[0]:
        stone_nn = stone_pos[1] + dn[d[move]]
        stone_nm = stone_pos[0] + dm[d[move]]

        if ord('A') <= stone_nm <= ord('H') and 1 <= stone_nn <= 8:
                stone_pos = [stone_nm, stone_nn]

        else:
            continue

    if ord('A') <= king_nm <= ord('H') and 1 <= king_nn <= 8:
        king_pos = [king_nm, king_nn]

king_pos[0] = chr(king_pos[0])
king_pos[1] = str(king_pos[1])
stone_pos[0] = chr(stone_pos[0])
stone_pos[1] = str(stone_pos[1])

print(''.join(king_pos))
print(''.join(stone_pos))
