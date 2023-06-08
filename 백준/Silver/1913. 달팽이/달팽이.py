n = int(input())
number = int(input())
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

arr = [[0] * n for _ in range(n)]
i, j = n // 2, n // 2
num = 1
dir = -1
y, x = 0, 0
while 1:
    if num > n ** 2:
        break
    arr[i][j] = num
    if arr[i][j] == number:
        y, x = i + 1, j + 1
    di, dj = direction[(dir + 1) % 4]
    if arr[i + di][j + dj] == 0:
        i += di
        j += dj
        dir += 1
    else:
        di, dj = direction[dir % 4]
        i += di
        j += dj
    num += 1
for i in arr:
    print(*i)
print(y, x)