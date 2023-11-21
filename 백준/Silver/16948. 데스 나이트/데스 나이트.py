from collections import deque

n = int(input())

lst = list(map(int, input().split()))
q = deque()
q.append((lst[0], lst[1], 0))

arr = [[0]*n for i in range(n)]
arr[lst[0]][lst[1]] = 1

def bfs(q):
    while q:
        i, j, ans = q.popleft()
        for di, dj in ((-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)):
            ni, nj = i + di, j + dj
            if ni == lst[2] and nj == lst[3]:
                return ans + 1
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 0:
                    arr[ni][nj] = 1
                    q.append((ni, nj, ans + 1))
    return -1
ans = bfs(q)
print(ans)