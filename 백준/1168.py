import sys
input = sys.stdin.readline

def init(segment_tree, node, s, e):
        if s == e:
            segment_tree[node] = 1
            return segment_tree[node]

        mid = (s + e) // 2
        segment_tree[node] = init(segment_tree, node * 2, s, mid) + init(segment_tree, node * 2 + 1, mid + 1, e)
        return segment_tree[node]

def update(segment_tree, s, e, target, node):
    segment_tree[node] -= 1

    if s == e:
        return

    mid = (s + e) // 2
    if target <= mid:
        return update(segment_tree, s, mid, target, node * 2)
    else:
        return update(segment_tree, mid + 1, e, target, node * 2 + 1)

def getSequence(segment_tree, s, e, node, seq):
    if s == e:
        return s

    mid = (s + e) // 2
    if seq <= segment_tree[node * 2]:
        return getSequence(segment_tree, s, mid, node * 2, seq)
    else:
        return getSequence(segment_tree, mid + 1, e, node * 2, seq - segment_tree[node*2])

n, k = map(int, input().rstrip().split())
segment_tree = [0 for _ in range(2 ** 18)]
result = []
init(segment_tree, 1, 1, n)
idx = 1
for i in range(n):
    num = n - i
    idx += k - 1

    if idx % num == 0:
        idx = num
    elif idx > num:
        idx = idx % num

    seq = getSequence(segment_tree, 1, n, 1, idx)
    update(segment_tree, 1, n, seq, 1)
    result.append(str(seq))
print("<",', '.join(result),'>', sep='')