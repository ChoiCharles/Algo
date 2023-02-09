import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(map(int, input().split()))
lst.sort()
si = 0
ei = n - 1
cnt = 0
while 1:
    if lst[si] + lst[ei] > m:
        ei -= 1
    elif lst[si] + lst[ei] < m:
        si += 1
    else:
        cnt += 1
        si += 1
    if ei == si:
        break
print(cnt)