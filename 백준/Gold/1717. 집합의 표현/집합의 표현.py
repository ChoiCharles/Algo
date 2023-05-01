import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if a == lst[a]:
        return a
    lst[a] = find(lst[a])
    return lst[a]

def union(a, b):
    fa, fb = find(a), find(b)
    if fa < fb:
        lst[fb] = fa
    elif fa > fb:
        lst[fa] = fb

def check(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return 1
    else:
        return 0

n, m = map(int, input().split())
lst = [0] * (n + 1)
for i in range(n + 1):
    lst[i] = i
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        union(b, c)
    else:
        if check(b, c):
            print('YES')
        else:
            print('NO')