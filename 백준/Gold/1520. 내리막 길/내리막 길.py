import sys
input = sys.stdin.readline

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
def dfs(i, j):
    if i == n - 1 and j == m - 1:
        return 1

    if res[i][j] != -1:
        return res[i][j]

    k = 0
    for di, dj in dir:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and arr[i][j] > arr[ni][nj]:
            k += dfs(ni, nj)
    res[i][j] = k
    return res[i][j]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = [[-1] * m for _ in range(n)]
ans = dfs(0, 0)
print(ans)