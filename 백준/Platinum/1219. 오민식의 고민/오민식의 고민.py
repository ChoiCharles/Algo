import sys
input = sys.stdin.readline

INF = int(21e8)
n, s, e, m = map(int, input().split())
edges = []
dist = [-INF] * n

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

lst = list(map(int, input().split()))
dist[s] = lst[s]

for i in range(n+101):
    for start, end, cost in edges:
        if dist[start] == -INF:
            continue
        elif dist[start] == INF:
            dist[end] = INF
        elif dist[end] < dist[start] + lst[end] - cost:
            dist[end] = dist[start] + lst[end] - cost
            if i >= n-1:
                dist[end] = INF
if dist[e] == -INF:
    print('gg')
elif dist[e] == INF:
    print('Gee')
else:
    print(dist[e])