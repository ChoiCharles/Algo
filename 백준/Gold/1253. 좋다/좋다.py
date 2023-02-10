import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0

for i in range(n):
    a = lst[:i] + lst[i+1:]
    left = 0
    right = len(a) - 1
    while left < right:
        s = a[left] + a[right]
        if s == lst[i]:
            cnt += 1
            break
        if s < lst[i]:
            left += 1
        else:
            right -= 1
print(cnt)