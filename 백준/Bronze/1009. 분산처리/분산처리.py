t = int(input())
for case in range(t):
    a, b = map(int, input().split())
    c = a
    if b == 0:
        print(1)
    elif b == 1:
        c = c % 10
    else:
        for i in range(b-1):
            c = (c * a)%10
    if c == 0:
        print(10)
    else:
        print(c)