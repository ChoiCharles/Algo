import heapq
import sys
input = sys.stdin.readline
n = int(input())
lst = []
res = 0
for i in range(n):
    a = int(input())
    heapq.heappush(lst, a)
cnt = heapq.heappop(lst)
heapq.heappush(lst, cnt)
cnt = 0
for i in range(n):
    a = heapq.heappop(lst)
    try:
        b = heapq.heappop(lst)
        cnt += a + b
        heapq.heappush(lst, a+b)
    except:
        break
print(cnt)