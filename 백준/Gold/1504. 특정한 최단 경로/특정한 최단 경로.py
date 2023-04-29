import sys
input = sys.stdin.readline

from collections import deque
def bfs(idx, a):
    global n, res, inf
    v = [[0, inf] for _ in range(n + 1)]
    q = deque()
    q.append(idx)
    v[idx][0] = 1
    v[idx][1] = 0
    while q:
        idx = q.popleft()
        for i in lst[idx]:
            target, cost = i
            if v[idx][1] + cost < v[target][1]:
                q.append(target)
                v[target][0] = 1
                v[target][1] = v[idx][1] + cost

    return v[a][1]

n, e = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for i in range(e):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))
v1, v2 = map(int, input().split())
root1 = [1, v1, v2, n]
root2 = [1, v2, v1, n]
R1 = 0
R2 = 0
inf = 21e8
for i in range(3):
    a = bfs(root1[i], root1[i+1])
    if a == inf:
        R1 = 0
        break
    R1 += a
for i in range(3):
    a = bfs(root2[i], root2[i+1])
    if a == inf:
        R2 = 0
        break
    R2 += a
if R1 == 0 and R2 == 0:
    print(-1)
else:
    res = min(R1, R2)
    print(res)