import sys
input = sys.stdin.readline

from collections import deque

cnt = 0
cnt_w = 0
def nor(level, x):
    global cnt
    q = deque()
    q.append((level, x))
    v[level][x] = 1

    while q:
        i, j = q.pop()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and v[ni][nj] == 0:
                if arr[i][j] == arr[ni][nj]:
                    v[ni][nj] = v[i][j]
                    q.append((ni, nj))
    cnt += 1

def anor(level, x):
    global cnt_w
    q = deque()
    q.append((level, x))
    v_w[level][x] = 1
    if arr[level][x] == 'B':
        while q:
            i, j = q.pop()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and v_w[ni][nj] == 0:
                    if arr[i][j] == arr[ni][nj]:
                        v_w[ni][nj] = v[i][j]
                        q.append((ni, nj))

    elif arr[level][x] == 'R' or arr[level][x] == 'G':
        while q:
            i, j = q.pop()
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and v_w[ni][nj] == 0:
                    if arr[ni][nj] != 'B':
                        v_w[ni][nj] = v[i][j]
                        q.append((ni, nj))
    cnt_w += 1

n = int(input())
arr = [list(input()) for _ in range(n)]
v = [[0] * n for _ in range(n)]
v_w = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if v[i][j] == 0:
            nor(i, j)
for i in range(n):
    for j in range(n):
        if v_w[i][j] == 0:
            anor(i, j)
print(cnt, cnt_w)