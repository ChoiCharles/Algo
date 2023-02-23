import sys
input = sys.stdin.readline
def bingo(y, x):
    global cnt
    dy = [[0, 0], [1, -1], [1, -1], [1, -1]]
    dx = [[1, -1], [0, 0], [-1, 1], [1, -1]]
    for i in range(4):
        flag = 0
        for j in range(2):
            for k in range(1, 5):
                if arr[y + dy[i][j] * k][x + dx[i][j] * k] == 0:
                    flag += 1
                else:
                    break
        if flag == 4:
            cnt += 1

lst = [[-1] * 7]
lst2 = [[-1] + list(map(int, input().split())) + [-1] for _ in range(5)]
arr = lst + lst2 + lst
cnt = 0
cnt2 = 0
for i in range(5):
    lst3 = list(map(int, input().split()))
    for j in range(5):
        a = lst3[j]
        cnt2 += 1
        for k in range(1, 6):
            for l in range(1, 6):
                if arr[k][l] == a:
                    arr[k][l] = 0
                    bingo(k, l)
        if cnt >= 3:
            break
    if cnt >= 3:
        break
print(cnt2)