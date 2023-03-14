import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a = int(input())
    lst.append((a, i))
a = sorted(lst)
ans = a[0][1] - lst[0][1]
for i in range(1, n):
    ans = max(ans, a[i][1] - lst[i][1])
print(ans+1)