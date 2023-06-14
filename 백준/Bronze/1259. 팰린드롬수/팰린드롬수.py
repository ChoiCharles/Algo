while 1:
    lst = list(map(int, input()))
    if len(lst) == 1 and lst[0] == 0:
        break
    start = 0
    end = len(lst) - 1
    flag = 1
    while start <= end:
        if lst[start] == lst[end]:
            start += 1
            end -= 1
        else:
            flag = 0
            break
    if flag:
        print('yes')
    else:
        print('no')