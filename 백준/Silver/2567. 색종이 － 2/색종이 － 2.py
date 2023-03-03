import sys
input = sys.stdin.readline

def asdf(arr):
    global MI, MJ, cnt
    for i in range(MI):
        for j in range(1, MJ):
            if abs(arr[i][j] - arr[i][j - 1]) == 1:
                cnt += 1

arr = [[0] * 101 for _ in range(101)]
n = int(input())
MI = 0
MJ = 0
for _ in range(n):
    y, x = map(int, input().split())
    MI = max(MI, y + 10)
    MJ = max(MJ, x + 10)
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] = 1
MI += 1
MJ += 1
cnt = 0
asdf(arr)
arr_t = list(map(list, zip(*arr)))
MI, MJ = MJ, MI
asdf(arr_t)
print(cnt)