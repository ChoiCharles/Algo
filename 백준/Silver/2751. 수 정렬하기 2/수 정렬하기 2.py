import sys
input = sys.stdin.readline

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst)//2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            lst[k] = right[j]
            k += 1
            j += 1
    elif j == len(right):
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
    return lst

n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
lst = mergesort(lst)
for i in lst:
    print(i)