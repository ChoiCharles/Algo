import sys
input = sys.stdin.readline

from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    visit[a] = 1

    while q:
        a = q.popleft()
        for i in g[a]:
            if visit[i] == 0:
                visit[i] = - visit[a]
                q.append(i)
            elif visit[i] == visit[a]:
                return 0
    return 1

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    g = [[] for _ in range(v + 1)]
    visit = [0 for _ in range(v + 1)]
    flag = 1
    for i in range(e):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(1, v + 1):
        if visit[i] == 0:
            flag = bfs(i)
        if flag == 0:
            break
    if flag == 1:
        print('YES')
    else:
        print('NO')