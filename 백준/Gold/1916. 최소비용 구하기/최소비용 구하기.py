import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
m = int(input())
lst = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
start, end = map(int, input().split())
INF = int(21e8)
heap = []
res = [INF] * (n + 1)
res[start] = 0
heappush(heap, (0, start))
while heap:
    c, now = heappop(heap)
    if c > res[end]:
        continue
    for next, cost in lst[now]:
        if c + cost < res[next]:
            res[next] = c + cost
            heappush(heap, (res[next], next))
print(res[end])