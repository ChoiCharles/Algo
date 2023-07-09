import sys
input = sys.stdin.readline

from collections import deque

def dijkstra(a):
    q = deque()
    q.append(a)
    v[a] = 0
    while q:
        a = q.popleft()
        for next, l in lst[a]:
            if v[next] > v[a] + l:
                v[next] = v[a] + l
                q.append(next)


inf = 21e8
n, d = map(int, input().split())
lst = [[] for _ in range(d + 1)]
v = [inf] * (d + 1)

for i in range(d):
    lst[i].append((i+1, 1))

for i in range(n):
    s, e, l = map(int, input().split())
    if e > d:
        continue
    lst[s].append((e, l))
dijkstra(0)
print(v[d])