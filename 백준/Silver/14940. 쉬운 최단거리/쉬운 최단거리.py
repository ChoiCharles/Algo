from collections import deque

def bfs(arr, y, x, n, m):
    q = deque()
    q.append((y, x, 0))
    while q:
        i, j, cnt = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == -1:
                    arr[ni][nj] = cnt + 1
                    q.append((ni, nj, cnt + 1))
                elif arr[ni][nj] != 0 and arr[ni][nj] > cnt + 1:
                    arr[ni][nj] = cnt + 1
                    q.append((ni, nj, cnt + 1))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
ans = [[-1] * m for i in range(n)]
y, x = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            y, x = i, j
        if arr[i][j] == 0:
            ans[i][j] = 0
ans[y][x] = 0
bfs(ans, y, x, n, m)
for i in ans:
    print(*i)