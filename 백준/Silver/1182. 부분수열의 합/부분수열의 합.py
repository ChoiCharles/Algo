def calc(lev, a):
    global ans
    if lev != 0 and a == s:
        ans += 1
    for i in range(lev, n):
        if not v[i]:
            v[i] = 1
            calc(i+1, a+lst[i])
            v[i] = 0

n, s = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0
v = [0] * n
calc(0, 0)
print(ans)