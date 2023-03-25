def asdf(n, y, x):
    global cnt
    if n < 1:
        return
    mid = int(n/2)
    flag = 0
    if mid <= y:
        flag += 2
    if mid <= x:
        flag += 1
    if flag == 1:
        cnt += mid**2
        asdf(mid, y, x - mid)
    elif flag == 2:
        cnt += (mid**2) * 2
        asdf(mid, y - mid, x)
    elif flag == 3:
        cnt += (mid ** 2) * 3
        asdf(mid, y - mid, x - mid)
    else:
        asdf(mid, y, x)
n, y, x = map(int, input().split())
cnt = 0
a = 2 ** n
asdf(a, y, x)
print(cnt)