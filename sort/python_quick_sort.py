def quick_sort(list):
    if len(list) > 1:
        pivot = list[0]

        left,mid,right = [], [], []

        for num in list[1:]:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)

        mid.append(pivot)

        return quick_sort(left)+mid+quick_sort(right)
    else:
        return list

if __name__=="__main__":
    numbers = [9,2,5,3,6,1,4,7,10,8]
    print(quick_sort(numbers))