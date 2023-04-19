import sys
input = sys.stdin.readline

from collections import deque

def bfs(arr):
    global q, z, res
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = arr[i][j] + 1
                    res = max(arr[ni][nj], res)
                    q.append((ni, nj))
                    z -= 1

m, n = map(int, input().split())
arr = []
z = 0
q = deque()
for i in range(n):
    lst = list(map(int, input().split()))
    z += lst.count(0)
    arr.append(lst)
    for j in range(m):
        if lst[j] == 1:
            q.append((i, j))
res = 0
bfs(arr)
if z:
    print(-1)
else:
    if res:
        print(res-1)
    else:
        print(res)