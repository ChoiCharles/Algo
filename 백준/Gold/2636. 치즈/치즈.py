import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((0, 0))
    v[0][0] = 1
    cnt = 0
    while q:
        i, j = q.popleft()
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if v[ni][nj] == 0:
                    if arr[ni][nj] == 1:
                        arr[ni][nj] = 0
                        cnt += 1
                    else:
                        q.append((ni, nj))
                    v[ni][nj] = 1

    return cnt

n, m = map(int, input().split())
arr = []
for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
tot = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tot += 1
t = 0
while 1:
    t += 1
    v = [[0] * m for _ in range(n)]
    cnt = bfs()
    tot -= cnt
    if not tot:
        print(t)
        print(tot + cnt)
        break