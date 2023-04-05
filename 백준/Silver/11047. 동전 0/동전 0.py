n, k = map(int, input().split())
lst = []
for i in range(n):
    a = int(input())
    lst.append(a)
lst = lst[::-1]
cnt = 0
for i in lst:
    if k == 0:
        break
    if i > k:
        continue
    a = divmod(k, i)
    cnt += a[0]
    k = a[1]
print(cnt)