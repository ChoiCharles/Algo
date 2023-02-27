import sys
input = sys.stdin.readline

n = int(input())
res = []
for i in range(n):
    lsta = list(map(int, input().split()))
    lstb = list(map(int, input().split()))
    a = lsta.pop(0)
    b = lstb.pop(0)
    lsta.sort(reverse = True)
    lstb.sort(reverse = True)
    if a >= b:
        flag = 0
        for i in range(a):
            try:
                if lsta[i] - lstb[i] >= 1:
                    res.append('A')
                    break
                elif lstb[i] - lsta[i] >= 1:
                    res.append('B')
                    break
                else:
                    flag += 1
            except:
                res.append('A')
        if flag >= b and a == b:
            res.append('D')
    else:
        flag = 0
        for i in range(b):
            try:
                if lsta[i] - lstb[i] >= 1:
                    res.append('A')
                    break
                elif lstb[i] - lsta[i] >= 1:
                    res.append('B')
                    break
                else:
                    flag += 1
            except:
                res.append('B')
        if flag >= b and a == b:
            res.append('D')
for i in res:
    print(i)