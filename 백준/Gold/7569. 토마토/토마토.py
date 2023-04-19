import sys
input = sys.stdin.readline

def bfs(arr):
    global q, res, z
    while q:
        i, j, k = q.popleft()
        for di, dj, dk in ((-1, 0, 0), (1, 0, 0), (0, -1, 0),
                           (0, 1, 0), (0, 0, -1), (0, 0, 1)):
            ni, nj, nk = i+di, j+dj, k+dk
            if 0<=ni<h and 0<=nj<n and 0<=nk<m:
                if arr[ni][nj][nk] == 0:
                    z -= 1
                    arr[ni][nj][nk] = arr[i][j][k] + 1
                    if arr[ni][nj][nk] > res:
                        res = arr[ni][nj][nk]
                    q.append((ni, nj, nk))

from collections import deque

q = deque()
z = 0
m, n, h = map(int, input().split())
arr = []
for i in range(h):
    lst = []
    for j in range(n):
        lst2 = list(map(int, input().split()))
        z += lst2.count(0)
        for k in range(m):
            if lst2[k] == 1:
                q.append((i, j, k))
        lst.append(lst2)
    arr.append(lst)
res = 0
bfs(arr)
if z>0:
    print(-1)
else:
    if res:
        print(res-1)
    else:
        print(res)