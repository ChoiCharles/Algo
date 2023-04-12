from collections import deque

def asdf(lst):
    res = 0
    k = 1
    while lst:
        a = lst.popleft()
        if a == '+':
            k = 1
        elif a == '-':
            k = 2
        else:
            if k == 1:
                res += a
            else:
                res -= a
    return res

lst = list(input())
equ = deque()
num = ''
temp = deque()
flag = 0
for i in lst:
    try:
        a = int(i)
        num += i
    except:
        if i == '+':
            if flag == 1:
                temp.append(int(num))
                temp.append(i)
            else:
                equ.append(int(num))
                equ.append(i)
        elif i == '-':
            if flag == 1:
                temp.append(int(num))
                Sum = asdf(temp)
                equ.append(Sum)
                equ.append(i)
                temp = deque()
            else:
                flag = 1
                equ.append(int(num))
                equ.append(i)
        num = ''
if flag:
    temp.append(int(num))
    Sum = asdf(temp)
    equ.append(Sum)
else:
    equ.append(int(num))
res = asdf(equ)
print(res)