while 1:
    lst = list(map(int, input().split()))
    c = 0
    idx = 0
    for i in range(len(lst)):
        if lst[i] > c:
            c = lst[i]
            idx = i
    c = lst.pop(idx)
    a = lst[0]
    b = lst[1]
    if c == 0 and a == 0 and b == 0:
        break
    if c ** 2 == (a ** 2) + (b ** 2):
        print('right')
    else:
        print('wrong')