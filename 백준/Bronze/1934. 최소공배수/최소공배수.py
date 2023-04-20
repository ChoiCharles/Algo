t = int(input())
for case in range(t):
    a, b = map(int, input().split())
    if a >= b:
        A = a
        B = b
    else:
        A = b
        B = a
    res = A % B
    A = B
    B = res
    while res:
        res = A % B
        A = B
        B = res
    print(int(a*b/A))