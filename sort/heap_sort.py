
def heapify(array):
    for i in range(len(array)):
        c = i
        while c != 0:
            root = (c-1) // 2
            if array[root] < array[c]:
                array[root], array[c] = array[c], array[root]
            c = root
    return array


def heap_sort(array):
    for i in range(len(array)-1, 0, -1):
        root = 0
        array[i], array[root] = array[root], array[i]
        array = heapify(array[:i]) + array[i:]

    return array


if __name__ == "__main__":
    numbers = [9,2,5,3,6,1,4,7,10,8]
    print(heap_sort(numbers))


