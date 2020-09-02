
def get_parents(parents, node):
    if parents[node] == node:
        return node
    return get_parents(parents, parents[node])

def union_parents(parents, a, b):
    a = get_parents(parents, a)
    b = get_parents(parents, b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def find_parents(parents, a, b):
    a = get_parents(parents,a)
    b = get_parents(parents,b)
    if a == b:
        return True
    return False



if __name__ == "__main__":
    parents = [x for x in range(10)]        #부모 노드
    union_parents(parents,1,4)      #node 1, 4
    union_parents(parents,2,5)      #node 2, 5

    print("node : 4 5",find_parents(parents,4,5))

    union_parents(parents,1,2)      #node 1, 2

    print("node : 4 5",find_parents(parents,4,5))