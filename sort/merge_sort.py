
def merge(left, right):
    l_index = 0
    r_index = 0
    merge_list = []

    while l_index < len(left) and r_index < len(right):
        if left[l_index] > right[r_index]:
            merge_list.append(right[r_index])
            r_index += 1
        else:
            merge_list.append(left[l_index])
            l_index += 1
    while l_index >= len(left) and r_index < len(right):
        merge_list.append(right[r_index])
        r_index += 1
    while l_index < len(left) and r_index >= len(right):
        merge_list.append(left[l_index])
        l_index += 1

    return merge_list

def merge_sort(numbers):
    length = len(numbers)
    if length > 1:
        l = merge_sort(numbers[:length//2])
        r = merge_sort(numbers[length//2:])
        return merge(l,r)
    else:
        return numbers

if __name__=="__main__":
    numbers = [9,2,5,3,6,1,4,7,10,8]
    print(merge_sort(numbers))