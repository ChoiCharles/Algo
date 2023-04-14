from collections import deque

def bfs(a):
    global m
    q = deque()
    q.append(a)

    while q:
        a = q.popleft()
        if a == m:
            return v[a]
        for i in (a-1, a+1, a*2):
            if 0 <= i <= 100000 and not v[i]:
                q.append(i)
                v[i] = v[a] + 1

n, m = map(int, input().split())
if n < m:
    M = 100001
    v = [0] * M
    res = bfs(n)
    print(res)
else:
    print(n-m)