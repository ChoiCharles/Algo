import sys
input = sys.stdin.readline

from collections import deque
def bfs(a):
    q = deque()
    q.append(a)
    while q:
        a = q.popleft()
        for i in lst[a]:
            if v[i] == 0:
                v[i] = v[a] + 1
                if v[i] > k:
                    continue
                q.append(i)
                if v[i] == k and i != x:
                    res.append(i)


n, m, k, x = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
v = [0] * (n+1)
v[0] = 1
res = []
bfs(x)
v[x] = 0
res.sort()
if res:
    for i in res:
        print(i)
else:
    print(-1)