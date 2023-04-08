n, m = map(int, input().split())
dic = {}
for i in range(n):
    a = input()
    dic[a] = 1
res = []
ans = 0
for i in range(m):
    a = input()
    b = dic.get(a, 0)
    if b == 1:
        ans += 1
        res.append(a)
res.sort()
print(ans)
for i in res:
    print(i)