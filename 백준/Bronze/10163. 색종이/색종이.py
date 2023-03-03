import sys
input = sys.stdin.readline

n = int(input())
arr = [[0] * 1001 for _ in range(1001)]
MI = 0
MJ = 0
for k in range(1, n + 1):
    i, j, ii, jj = map(int, input().split())
    MI = max(MI, i + ii)
    MJ = max(MJ, j + jj)
    for y in range(i, i + ii):
        for x in range(j, j + jj):
            arr[y][x] = k
for k in range(1, n + 1):
    cnt = 0
    for i in range(MI + 1):
        for j in range(MJ + 1):
            if arr[i][j] == k:
                cnt += 1
    print(cnt)