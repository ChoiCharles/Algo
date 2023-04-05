import sys
input = sys.stdin.readline

import heapq

n = int(input())
pos = []
pos_n = 0
neg = []
neg_n = 0
for i in range(n):
    a = int(input())
    if a <= 0:
        heapq.heappush(neg, a)
        neg_n += 1
    elif a > 0:
        heapq.heappush(pos, -a)
        pos_n += 1
res = []
while neg_n > 1:
    a = heapq.heappop(neg)
    b = heapq.heappop(neg)
    res.append(a * b)
    neg_n -= 2
while pos_n > 1:
    a = heapq.heappop(pos)
    b = heapq.heappop(pos)
    pos_n -= 2
    if a != -1 and b != -1:
        res.append(a * b)
    else:
        res.append(-a)
        res.append(-b)
ans = sum(res)
if neg_n == 1:
    ans += neg[0]
if pos_n == 1:
    ans -= pos[0]
print(ans)