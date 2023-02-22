import sys
input = sys.stdin.readline

from collections import deque
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
def bfs(y, x):
    global cnt, n, m
    q = deque()
    q.append([y, x])
    arr[y][x] = 0
    while 1:
        try:
            y, x = q.popleft()
        except:
            cnt += 1
            break
        for i in range(4):
            if arr[y + dy[i]][x + dx[i]] == 1:
                q.append([y + dy[i], x + dx[i]])
                arr[y + dy[i]][x + dx[i]] = 0
T = int(input())
for test_case in range(T):
    m, n, k = map(int, input().split())
    arr = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y + 1][x + 1] = 1
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == 1:
                bfs(i, j)
    print(cnt)