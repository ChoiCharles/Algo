import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
a = 0
s = [0]
for k in range(n):
    a += lst[k]
    s.append(a)
for k in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])