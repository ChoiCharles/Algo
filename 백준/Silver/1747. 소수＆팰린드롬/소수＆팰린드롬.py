def asdf(a):
    lst = list(str(a))
    start = 0
    end = len(lst)-1
    while start < end:
        if lst[start] != lst[end]:
            return 0
        start += 1
        end -= 1
    return 1

n = int(input())
lst = [True] * (10000000)
res = 0
for i in range(2, 10000000):
    if lst[i]:
        if i >= n:
            if asdf(i):
                res = i
                break
        for j in range(i+i, 10000000, i):
            lst[j] = False
print(res)