def asdf(i):
    mid = n // 2
    start = 0
    end = n
    while 1:
        if i < A[mid]:
            if mid == end:
                break
            mid, end = (mid + start) // 2, mid
            continue
        elif i > A[mid]:
            if mid == start:
                break
            mid, start = (end + mid) // 2, mid
            continue
        else:
            return print(1)
    return print(0)

n = int(input())
A = list(map(int, input().split()))
m = int(input())
X = list(map(int, input().split()))
A.sort()
for i in X:
    asdf(i)