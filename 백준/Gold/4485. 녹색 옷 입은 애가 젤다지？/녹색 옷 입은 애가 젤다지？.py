import sys
input = sys.stdin.readline

from collections import deque

def dijkstra():
    q = deque()
    q.append((0, 0))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                k = v[i][j] + arr[ni][nj]
                if k < v[ni][nj]:
                    q.append((ni, nj))
                    v[ni][nj] = k

inf = 21e8
n = int(input())
case = 0
while n:
    case += 1
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[inf] * n for _ in range(n)]
    v[0][0] = arr[0][0]
    dijkstra()
    print(f'Problem {case}: {v[n-1][n-1]}')
    n = int(input())