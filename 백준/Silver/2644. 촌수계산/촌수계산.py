from collections import deque

def bfs(a, b):
    q = deque()
    q.append(a)
    while q:
        a = q.popleft()
        for i in lst[a]:
            if v[i] == 0:
                q.append(i)
                v[i] = v[a] + 1
                if i == b:
                    return v[i]
    return -1

n = int(input())
lst = [[] for _ in range(n + 1)]
v = [0] * (n + 1)
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
res = bfs(a, b)
print(res)