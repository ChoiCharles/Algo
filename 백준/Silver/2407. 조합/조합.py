from fractions import Fraction
def fac(i):
    if i == 1:
        return 1
    return i * fac(i - 1)

a, b = map(int, input().split())
x = fac(a)
y = fac(a - b) * fac(b)
print(Fraction(x//y))