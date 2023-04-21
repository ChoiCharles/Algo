def asdf(a, b):
    if b == 0:
        return a
    return asdf(b, a%b)

a, b = map(int, input().split())
if a >= b:
    res = asdf(a, b)
else:
    res = asdf(b, a)
print('1'*res)