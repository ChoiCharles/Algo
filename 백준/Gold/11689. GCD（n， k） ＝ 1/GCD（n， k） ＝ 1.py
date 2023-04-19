import math

n = int(input())
res = n
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        res -= res / i
        while n % i == 0:
            n /= i
if n > 1:
    res -= res / n
print(int(res))