def dfs(a, k):
    global res
    if k >= b:
        if res >= k:
            res = k
            return
        return
    for i in range(a, n):
        if res == b:
            return
        if v[i] == 0:
            v[i] = 1
            dfs(i + 1, k + lst[i])
            v[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    n, b = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
    v = [0] * n
    res = 300000
    dfs(0, 0)
    print(f'#{test_case} {res-b}')