def dfs(a):
    global cnt, flag
    if cnt == 5:
        flag = 1
        return
    for i in lst[a]:
        if v[i] == 0:
            v[i] = 1
            cnt += 1
            dfs(i)
            cnt -= 1
            v[i] = 0
        if flag == 1:
            break

n, m = map(int, input().split())
lst = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
flag = 0
for i in range(n):
    v = [0] * n
    v[i] = 1
    cnt = 1
    dfs(i)
if flag == 1:
    print(1)
else:
    print(0)