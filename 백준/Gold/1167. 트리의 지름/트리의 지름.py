def dfs(a, c):
    global res, r_idx
    for i in range(len(lst[a])):
        if v[lst[a][i]] == 0:
            v[lst[a][i]] = 1
            dfs(lst[a][i], c+lst2[a][i])
            v[lst[a][i]] = 0
    if c > res:
        res = c
        r_idx = a

n = int(input())
lst = [[] for _ in range(n+1)]
lst2 = [[] for _ in range(n+1)]
for i in range(n):
    a = list(map(int, input().split()))
    idx = a.pop(0)
    j = 0
    while 1:
        if a[j] == -1:
            break
        lst[idx] += [a[j]]
        j += 1
        lst2[idx] += [a[j]]
        j += 1
v = [0] * (n+1)
res = 0
r_idx = 0
v[1] = 1
dfs(1, 0)
v = [0] * (n+1)
v[r_idx] = 1
dfs(r_idx, 0)
print(res)