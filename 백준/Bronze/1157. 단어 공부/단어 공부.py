st = list(input())
if len(st) == 1:
    print(st[0].upper())
else:
    dic = {}
    for i in st:
        a = i.upper()
        if dic.get(a, 0):
            dic[a] += 1
        else:
            dic[a] = 1
    dic = sorted(dic.items(), key=lambda x:x[1])
    if dic[-1][1] == dic[-2][1]:
        print('?')
    else:
        print(dic[-1][0])