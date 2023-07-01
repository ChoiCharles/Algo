import sys
input = sys.stdin.readline

from collections import deque

def bfs(i, j):
    q = deque()
    q.append((i, j))
    v[i][j] = 1
    cnt = 1
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1 and v[ni][nj] == 0:
                    q.append((ni, nj))
                    v[ni][nj] = 1
                    cnt += 1
    return cnt

n, m, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
v = [[0] * m for _ in range(n)]
MAX = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and v[i][j] == 0:
            cnt = bfs(i, j)
            MAX = max(MAX, cnt)
print(MAX)