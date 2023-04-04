import sys
input = sys.stdin.readline
sys.setrecursionlimit(100100)

def dfs(a):
    global temp, res

    if v[a] == 0:
        v[a] = 1
        temp += [a]
        dfs(lst[a])
        return
    if a in temp:
        idx = temp.index(a)
        temp = temp[idx:]
        res -= len(temp)
        return

for test_case in range(1, int(input())+1):
    n = int(input())
    res = n
    lst = [0] + list(map(int, input().split()))
    v = [0] * (n+1)
    for i in range(1, n+1):
        if lst[i] == i:
            v[i] = 1
            res -= 1
    for i in range(1, n+1):
        a = lst[i]
        if v[i] == 0:
            v[i] = 1
            temp = [i]
            dfs(a)
    print(res)