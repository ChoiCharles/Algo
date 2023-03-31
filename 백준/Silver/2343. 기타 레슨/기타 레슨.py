n, m = map(int, input().split())
lst = list(map(int, input().split()))
start = max(lst)
end = sum(lst)
while start <= end:
    mid = int((start + end) // 2)
    a = 0
    k = 0
    for i in range(n):
        if a + lst[i] > mid:
            a = 0
            k += 1
        a += lst[i]
    if a > 0:
        k += 1
    if k > m:
        start = mid + 1
    else:
        end = mid - 1
print(start)