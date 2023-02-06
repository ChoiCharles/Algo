n = int(input())
lst = list(map(int, input().split()))
for i in range(n):
    for j in range(i, n):
        if lst[i] < lst[j]:
            lst[j], lst[i] = lst[i], lst[j]
m = lst[0]
s = 0
for i in range(n):
    lst[i] = lst[i] / m * 100
    s += lst[i]
print(s/n)