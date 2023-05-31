from collections import deque

def bfs(i, j, num):
    q = deque()
    q.append((i, j))
    arr[i][j] = num
    count = 1
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] == 1:
                    q.append((ni, nj))
                    arr[ni][nj] = num
                    count += 1
    return count


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
num = -1
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt = bfs(i, j, num)
            ans.append(cnt)
            num -= 1
print(-num - 1)
ans.sort()
for i in ans:
    print(i)