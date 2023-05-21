import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    lst = list(input())
    res = 0
    k = 0
    for j in lst:
        if j == 'O':
            k += 1
            res += k
        else:
            k = 0
    print(res)