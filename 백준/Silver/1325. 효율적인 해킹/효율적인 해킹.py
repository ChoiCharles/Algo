import sys
input = sys.stdin.readline
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    v[a] = 1
    while q:
        a = q.popleft()
        for i in lst[a]:
            if v[i] == 0:
                q.append(i)
                res[i] += 1
                v[i] = 1

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
res = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)

for i in range(1, n + 1):
    v = [0] * (n + 1)
    bfs(i)

MAX = 0
for i in range(1, n + 1):
    MAX = max(MAX, res[i])

for i in range(1, n + 1):
    if res[i] == MAX:
        print(i, end=' ')