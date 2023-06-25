import sys
input = sys.stdin.readline

n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
dp = [0] * (n + 1)

M = 0
for i in range(n):
    M = max(M, dp[i])
    if t[i] + i > n:
        continue
    dp[t[i] + i] = max(dp[i + t[i]], p[i] + M)
print(max(dp))