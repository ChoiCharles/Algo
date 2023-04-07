import sys
input = sys.stdin.readline

import heapq

n = int(input())
lst = []
for i in range(n):
    a = int(input())
    if a == 0:
        try:
            b = heapq.heappop(lst)
            print(b)
        except:
            print(0)
    else:
        heapq.heappush(lst, a)