import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    global cnt, now_zero, iceberg
    # next_i, next_j = -1, -1
    v[i][j] = 1
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:
            if arr[ni][nj] <= 0 and v[ni][nj] == 0:
                arr[i][j] -= 1
            if arr[ni][nj] > 0 and v[ni][nj] == 0:
                # next_i, next_j = ni, nj
                dfs(ni, nj)
    if arr[i][j] <= 0:
        now_zero += 1
    else:
        iceberg += 1
    # if next_i != -1 and next_j != -1:
    #     dfs(next_i, next_j)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
tot = 0
for i in arr:
    for j in i:
        if j != 0:
            tot += 1
cnt = 0
res = 0
while 1:
    flag = 0
    v = [[0] * m for _ in range(n)]
    now_zero = 0
    iceberg = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                dfs(i, j)
                flag = 1
                break
        if flag == 1:
            break
    if now_zero + iceberg == tot and iceberg != 0:
        cnt += 1
        tot = iceberg
    elif now_zero == tot:
        cnt = 0
        break
    else:
        break
print(cnt)