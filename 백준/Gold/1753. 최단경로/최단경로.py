import sys
input = sys.stdin.readline
from heapq import heappop, heappush

V, E = map(int, input().split())
lst = [[] for _ in range(V + 1)]
start = int(input())
for i in range(E):
    u, v, w = map(int, input().split())
    lst[u].append((v, w))
INF = 21e8
root = [INF] * (V + 1)
root[start] = 0
heap = []
heappush(heap, (0, start))
visit = [0] * (V + 1)
while heap:
    now = heappop(heap)
    if visit[now[1]]:
        continue
    visit[now[1]] = 1
    for next, L in lst[now[1]]:
        if root[next] > L + now[0]:
            root[next] = L + now[0]
            heappush(heap, (root[next], next))
for i in range(1, V + 1):
    if visit[i]:
        print(root[i])
    else:
        print('INF')