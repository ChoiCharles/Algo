n, k = map(int, input().split())
lst = [[0] * (k+1) for _ in range(n+1)]
for i in range(n):
    w, v = map(int, input().split())
    for j in range(k+1):
        if j < w:
            lst[i+1][j] = lst[i][j]
        elif j == w:
            lst[i+1][j] = v
            lst[i+1][j] = max(lst[i][j], lst[i+1][j])
        else:
            lst[i+1][j] = v + lst[i][j-w]
            lst[i+1][j] = max(lst[i][j], lst[i+1][j])
print(lst[-1][-1])