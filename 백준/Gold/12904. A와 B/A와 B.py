a = list(input())
b = list(input())
a_n = len(a)
b_n = len(b)
flag = 0
while 1:
    if b[-1] == 'A':
        b.pop()
        b_n -= 1
    elif b[-1] == 'B':
        b.pop()
        b.reverse()
        b_n -= 1
    if a_n == b_n and a == b:
        flag = 1
        break
    elif a_n > b_n:
        break
if flag:
    print(1)
else:
    print(0)