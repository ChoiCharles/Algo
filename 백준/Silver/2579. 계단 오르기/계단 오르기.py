import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
dp = [0] * n
if n <= 2:
    print(sum(lst))
else:
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    for i in range(2, n):
        dp[i] = max(lst[i] + lst[i - 1] + dp[i - 3], lst[i] + dp[i - 2])
    print(dp[n - 1])