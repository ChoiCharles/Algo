import sys
input = sys.stdin.readline

n, m = map(int, input().split())
y, x, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0
while 1:
    if arr[y][x] == 0:
        arr[y][x] = 2
        ans += 1
    flag = 0
    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if arr[ny][nx] == 0:
            flag = 1
            break
    if flag == 0:
        dy, dx = direction[(dir - 2) % 4]
        if arr[y + dy][x + dx] == 1:
            break
        y += dy
        x += dx
    while flag:
        dir -= 1
        if dir < 0:
            dir += 4
        dy, dx = direction[dir % 4]
        if arr[y + dy][x + dx] == 0:
            y += dy
            x += dx
            break

print(ans)