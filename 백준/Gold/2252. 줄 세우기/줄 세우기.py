import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
edge = [0] * (n + 1)
for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    edge[b] += 1

q = deque()

for i in range(1, n + 1):
    if edge[i] == 0:
        q.append(i)
while q:
    a = q.popleft()
    print(a, end = ' ')
    for i in lst[a]:
        edge[i] -= 1
        if edge[i] == 0:
            q.append(i)
