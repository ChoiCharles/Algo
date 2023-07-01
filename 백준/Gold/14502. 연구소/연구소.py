from collections import deque
from copy import deepcopy

def bfs():
    arr_copy = deepcopy(arr)
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if arr_copy[ni][nj] == 0:
                    arr_copy[ni][nj] = 2
                    q.append((ni, nj))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr_copy[i][j] == 0:
                cnt += 1
    return cnt

def wall(c):
    global MAX
    if c == 3:
        res = bfs()
        MAX = max(MAX, res)
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(c + 1)
                arr[i][j] = 0

n, m = map(int, input().split())
arr = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
MAX = 0
wall(0)
print(MAX)