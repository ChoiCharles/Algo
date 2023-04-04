import sys
input = sys.stdin.readline

from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    v[a][0] = 1
    while q:
        a = q.popleft()
        for idx, c in lst[a]:
            if v[idx][0] == 0:
                v[idx][0] = idx
                v[idx][1] = v[a][1] + c
                q.append(idx)

n = int(input())
lst = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))
v = [[0, 0] for _ in range(n + 1)]
v[0][0] = 1
bfs(1)
lst2 = sorted(v, key = lambda x:x[1], reverse=True)
v = [[0, 0] for _ in range(n + 1)]
v[0][0] = 1
bfs(lst2[0][0])
res = sorted(v, key = lambda x:x[1], reverse=True)
print(res[0][1])