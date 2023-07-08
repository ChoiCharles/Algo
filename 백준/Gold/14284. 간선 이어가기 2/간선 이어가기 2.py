import sys
input = sys.stdin.readline

from collections import deque

def dijkstra(idx):
    q = deque()
    q.append(idx)
    while q:
        idx = q.popleft()
        for next, cost in arr[idx]:
            next_cost = v[idx] + cost
            if v[next] > next_cost:
                q.append(next)
                v[next] = next_cost


n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
s, t = map(int, input().split())
inf = 21e8
v = [inf] * (n+1)
v[s] = 0
dijkstra(s)
print(v[t])