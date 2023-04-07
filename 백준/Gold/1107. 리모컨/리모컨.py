def dfs(lev, cnt, p=[]):
    global N, res, n
    if lev == N - 1 and lev != 0:
        a = int(''.join(p))
        b = cnt + abs(a - n)
        res = min(res, b)
    elif lev == N:
        a = int(''.join(p))
        b = cnt + abs(a - n)
        res = min(res, b)
    elif lev == N+1:
        a = int(''.join(p))
        b = cnt + abs(a - n)
        res = min(res, b)
        return
    for i in btn:
        dfs(lev+1, cnt + 1, p + [str(i)])

n = int(input())
m = int(input())
btn = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if m != 0: 
    a = list(map(int, input().split()))
    for i in a:
        btn.remove(i)
N = len(str(n))
res = abs(n - 100)
if m != 10: dfs(0, 0)
print(res)