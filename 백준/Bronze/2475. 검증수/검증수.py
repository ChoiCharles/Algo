lst = list(map(int, input().split()))
n = 0
for i in lst:
    n += i ** 2
print(n%10)