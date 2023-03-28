n = int(input())
lst = list(map(int, input().split()))
lst.sort()
res = 0
i = 0
while n:
    res += lst[i] * n
    n -= 1
    i += 1
print(res)