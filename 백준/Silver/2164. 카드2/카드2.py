import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque()
for i in range(1, n + 1):
    q.append(i)
k = 1
a = q.popleft()
while q:
    if k % 2 == 0:
        q.append(a)
    a = q.popleft()
    k += 1
print(a)