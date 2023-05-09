import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
indegree = [0] * (n + 1)
lst = [[] for _ in range(n + 1)]
lst_rev = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst_rev[b].append((a, c))
    indegree[b] += 1
start, end = map(int, input().split())
q = deque()
q.append(start)
res = [0] * (n + 1)
while q:
    a = q.popleft()
    for i in lst[a]:
        indegree[i[0]] -= 1
        res[i[0]] = max(res[i[0]], res[a] + i[1])
        if indegree[i[0]] == 0:
            q.append(i[0])
ans = 0
v = [0] * (n + 1)
q.clear()
q.append(end)
v[end] = 1
while q:
    a = q.popleft()
    for i in lst_rev[a]:
        if res[a] == i[1] + res[i[0]]:
            ans += 1
            if not v[i[0]]:
                v[i[0]] = 1
                q.append(i[0])
print(res[end])
print(ans)