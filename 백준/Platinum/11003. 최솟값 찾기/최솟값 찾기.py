import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

deq = deque()
for i in range(n):
    while deq and deq[-1][1] > lst[i]:
        deq.pop()
    deq.append([i, lst[i]])
    if deq[0][0] <= i - l:
        deq.popleft()
    print(deq[0][1], end = ' ')