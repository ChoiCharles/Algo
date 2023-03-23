import sys
input = sys.stdin.readline

def find(a):
    if lst[a] == 0:
        return a
    res = find(lst[a])
    return res

def union(a, b):
    fa, fb = find(a), find(b)
    if fa ==fb:
        return
    lst[fb] = fa

n, m = map(int, input().split())
lst = [0] * (n+1)
for i in range(m):
    u, v = map(int, input().split())
    union(u, v)
print(lst.count(0)-1)