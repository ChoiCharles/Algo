import sys
sys.setrecursionlimit((10**5))
input = sys.stdin.readline

def dfs(y, x):
    global i
    if arr[y][x] <= i:
        v[y][x] = -1
        return
    for dy, dx in ((1, 0), (-1, 0), (0, -1), (0, 1)):
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and v[ny][nx] == 0:
            v[ny][nx] = 1
            dfs(ny, nx)

n = int(input())
m = 0
arr = []
for _ in range(n):
    lst = list(map(int, input().split()))
    a = max(lst)
    m = max(m, a)
    arr.append(lst)
MAX = 1
for i in range(1, m):
    v = [[0] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if v[j][k] == 0:
                v[j][k] = 1
                dfs(j, k)
                if v[j][k] == -1:
                    continue
                cnt += 1
    MAX = max(cnt, MAX)
print(MAX)