M, N = map(int, input().split())
m, n = int(M**0.5)+1, int(N**0.5)
lst = [True] * (n+1)
a = int(n**0.5)
for i in range(2, a+1):
    if lst[i] == True:

        for j in range(i+i, n+1, i):
            lst[j] = False
res = 0
for i in range(2, n+1):
    if lst[i] and i > 1:
        a = i
        while i <= N/a:
            if i >= M/a:
                res += 1
            a *= i
print(res)