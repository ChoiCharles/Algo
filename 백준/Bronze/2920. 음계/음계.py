lst = list(map(int, input().split()))
a = lst[0]
flag = 0
for i in range(1, 8):
    if lst[i] - a == 1:
        flag = 1
    elif lst[i] - a == -1:
        flag = -1
    else:
        flag = 0
        break
    a = lst[i]
if flag == 1:
    print('ascending')
elif flag == -1:
    print('descending')
else:
    print('mixed')