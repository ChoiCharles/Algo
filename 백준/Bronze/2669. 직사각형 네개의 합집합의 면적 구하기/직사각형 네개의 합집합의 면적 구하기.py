import sys
input = sys.stdin.readline

arr = [[0]*100 for _ in range(100)]
for k in range(4):
    i, j, i2, j2 = map(int, input().split())
    for l in range(i, i2):
        for m in range(j, j2):
            arr[l][m] = 1
cnt = 0
for i in arr:
    for j in i:
        if j == 1:
            cnt += 1
print(cnt)