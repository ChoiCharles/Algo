import sys
input = sys.stdin.readline

t = int(input())
for testcase in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]
    lst.sort()
    top = 0
    res = 1
    for i in range(1, n):
        if lst[i][1] < lst[top][1]:
            top = i
            res += 1
    print(res)