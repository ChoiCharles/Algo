import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
indegree = [0] * (n + 1)
build = [0] * (n + 1)
arr = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    lst = list(map(int, input().split()))
    build[i] = lst[0]
    idx = 1
    while 1:
        if lst[idx] == -1:
            break
        arr[lst[idx]].append(i)
        indegree[i] += 1
        idx += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

res = [0] * (n + 1)
while q:
    a = q.popleft()
    for i in arr[a]:
        indegree[i] -= 1
        res[i] = max(res[i], res[a] + build[a])
        if indegree[i] == 0:
            q.append(i)
for i in range(1, n + 1):
    print(res[i] + build[i])