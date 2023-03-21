import sys
input = sys.stdin.readline

def mergesort(lst):
    global swap
    # 재귀함수 종료지점
    if len(lst) <= 1:
        return lst
    # 병합정렬을 하기 위해 리스트를 2개의 그룹으로 나눈다
    mid = len(lst)//2
    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])
    i = 0   # 왼쪽 그룹 인덱스
    j = 0   # 오른쪽 그룹 인덱스
    k = 0   # 정렬이 진행된 리스트의 인덱스
    # 정렬 시작
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            swap += j - k + mid
            j += 1
        k += 1
    # 한쪽 그룹의 값만이 남았을 때
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
lst = list(map(int, input().split()))
swap = 0
lst = mergesort(lst)
print(swap)