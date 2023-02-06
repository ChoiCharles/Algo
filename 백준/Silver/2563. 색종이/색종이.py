import sys

input = sys.stdin.readline

arr = [[0]*100 for _ in range(100)]
T = int(input())
for test_case in range(1, T + 1):
    y, x = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] += 1
cnt = 0
for i in arr:
    for j in i:
        if j > 0:
            cnt += 1
print(cnt)