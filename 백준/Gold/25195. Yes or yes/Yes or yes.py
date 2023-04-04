import sys
input = sys.stdin.readline

from collections import deque
def bfs(a):
    global res
    q = deque()
    q.append(a)
    while q:
        a = q.popleft()
        if lst[a]:
            if lst[a][0] == -1:
                continue
            for i in lst[a]:
                q.append(i)
        else:
            res = 1
            return

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
s = int(input())
sn = list(map(int, input().split()))
for i in sn:
    lst[i].insert(0, -1)
res = 0
bfs(1)
if res == 1:
    print('yes')
else:
    print('Yes')