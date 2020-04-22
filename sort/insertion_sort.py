import sys

def insertion_sort(list):
    for i,v in enumerate(list):
        while i-1 >= 0 and list[i-1] >= list[i]:
            list[i],list[i-1] = list[i-1],list[i]
            i -= 1
    return list

if __name__ == "__main__":
    numbers = list(map(int, sys.stdin.readline().split()))
    print(insertion_sort(numbers))
