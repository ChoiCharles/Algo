def calc(lev, a):
    global Max, Min
    if lev == n:
        Max = max(Max, a)
        Min = min(Min, a)
    for i in range(4):
        if op[i]:
            op[i] -= 1
            if i == 0:
                calc(lev+1, a + lst[lev])
            elif i == 1:
                calc(lev + 1, a - lst[lev])
            elif i == 2:
                calc(lev + 1, a * lst[lev])
            elif i == 3:
                if a >= 0:
                    b = divmod(a, lst[lev])
                    c = b[0]
                else:
                    b = divmod(-a, lst[lev])
                    c = -b[0]
                calc(lev + 1, c)
            op[i] += 1

n = int(input())
lst = list(map(int, input().split()))
op = list(map(int, input().split()))
Max, Min = -int(21e8), int(21e8)
calc(1, lst[0])
print(Max)
print(Min)