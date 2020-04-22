def quick_sort(list,start,end):

    if start >= end:
        return

    pivot = list[start]
    left = start + 1
    right = end

    while left <= right:
        while left <= end and list[left] <= pivot:
            left += 1

        while list[right] >= pivot and right > start:
            right -= 1

        if left > right:
            list[right], list[start] = list[start],list[right]
        else:
            list[left], list[right] = list[right],list[left]

    quick_sort(list,start,right-1)
    quick_sort(list,right+1,end)




if __name__=="__main__":
    numbers = [9,2,5,3,6,1,4,7,10,8]
    quick_sort(numbers,0,len(numbers)-1)
    print(numbers)