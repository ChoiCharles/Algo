import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n, m, k = map(int, input().split())
lst = [[] for _ in range(n + 1)]
INF = int(21e8)
for i in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))

start = 1
root = [[INF] * k for _ in range(n + 1)]
root[1][0] = 0
heap = []
heappush(heap, (0, start))
while heap:
    cost, now = heappop(heap)
    for next, next_cost in lst[now]:
        next_cost += cost
        if root[next][k-1] > next_cost:
            root[next][k-1] = next_cost
            root[next].sort()
            heappush(heap, (next_cost, next))
for i in range(1, n + 1):
    if root[i][k-1] == INF:
        print(-1)
    else:
        print(root[i][k-1])