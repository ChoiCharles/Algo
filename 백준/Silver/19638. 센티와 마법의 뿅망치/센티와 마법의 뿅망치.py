import sys
input = sys.stdin.readline

from queue import PriorityQueue

q = PriorityQueue()
n, h, t = map(int, input().split())
ans = 0
flag = 0
cnt = 0
for i in range(n):
    a = int(input())
    q.put(-a)
for i in range(t):
    a = q.get() * (-1)
    if a < h:
        ans = cnt
        flag = 1
        print('YES')
        break
    if a > 1:
        a = a // 2
        cnt += 1
    else:
        q.put(-a)
        break
    q.put(-a)
if not flag and not ans:
    a = q.get() * (-1)
    if a < h:
        print('YES')
        ans = t
    else:
        ans = a
        print('NO')
print(ans)