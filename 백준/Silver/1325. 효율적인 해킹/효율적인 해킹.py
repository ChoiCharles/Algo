import sys
input = sys.stdin.readline
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    v[a] = 1
    cnt = 1
    while q:
        a = q.popleft()
        for i in lst[a]:
            if v[i] == 0:
                q.append(i)
                cnt += 1
                v[i] = 1
    return cnt

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    lst[b].append(a)

MAX = 0
for i in range(1, n + 1):
    v = [0] * (n + 1)
    res = bfs(i)
    if MAX < res:
        MAX = res
        ans = []
        ans.append(i)
    elif MAX == res:
        ans.append(i)

print(*ans)