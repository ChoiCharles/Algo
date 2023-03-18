import sys
input = sys.stdin.readline

from collections import deque

n, m, v = map(int, input().split())
lst = [[] for _ in range(n+1)]
v_d = [0]*(n+1)

def dfs(a):
    print(a, end = ' ')
    v_d[a] = 1
    for i in lst[a]:
        if i != 0 and v_d[i] == 0:
            dfs(i)

v_b = [0]*(n+1)
def bfs(a):
    q = deque()
    q.append(a)
    v_b[a] = 1

    while q:
        b = q.popleft()
        print(b, end = ' ')
        for i in lst[b]:
            if v_b[i] == 0:
                q.append(i)
                v_b[i] = 1

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
for i in lst:
    i.sort()
dfs(v)
print()
bfs(v)