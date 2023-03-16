
def dfs(cnt, i=0, j=0):
    global ans

    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c:
            if v[arr[ni][nj]] == 0:
                v[arr[ni][nj]] = 1
                dfs(cnt + 1, ni, nj)
                v[arr[ni][nj]] = 0
    ans = max(ans, cnt)
    return ans

r, c = map(int, input().split())
arr = [list(map(lambda x:ord(x) - 65, input())) for _ in range(r)]
v = [0] * 26
v[arr[0][0]] = 1
ans = 0
dfs(1)
print(ans)