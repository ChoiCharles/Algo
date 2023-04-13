m, n = map(int, input().split())
lst = [True] * (n+1)
a = int(n**0.5)
for i in range(2, a + 1):
    if lst[i] == True:
        for j in range(i+i, n+1, i):
            lst[j] = False
for i in range(m, n + 1):
    if lst[i] and i > 1:
        print(i)