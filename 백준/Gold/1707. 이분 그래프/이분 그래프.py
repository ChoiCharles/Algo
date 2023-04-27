import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(a):
    global res
    v[a] = 1
    for i in lst[a]:
        if res:
            return
        if not v[i]:
            c[i] = (c[a] + 1) % 2
            dfs(i)
        elif c[i] == c[a]:
            res = 1
            return

t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    lst = [[] for _ in range(n + 1)]
    for i in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    res = 0
    v = [0] * (n + 1)
    c = [0] * (n + 1)
    for i in range(1, n + 1):
        dfs(i)
        if res:
            break
    if res:
        print('NO')
    else:
        print('YES')