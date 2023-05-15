import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
INF = int(21e8)
res = [INF] * (n + 1)
for i in range(m):
    a, b, c = map(int, input().split())
    lst.append((a, b, c))
res[1] = 0
for i in range(n - 1):
    for now, next, next_cost in lst:
        if res[now] != INF and res[next] > res[now] + next_cost:
            res[next] = res[now] + next_cost

mcycle = False

for now, next, next_cost in lst:
    if res[now] != INF and res[next] > res[now] + next_cost:
        mcycle = True
if mcycle:
    print(-1)
else:
    for i in range(2, n + 1):
        if res[i] != INF:
            print(res[i])
        else:
            print(-1)