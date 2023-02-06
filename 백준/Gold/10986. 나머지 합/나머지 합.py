import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))
D = [0] * n
D[0] = A[0]
result = [0] * m
for i in range(1, n):
    D[i] = D[i - 1] + A[i]
for i in range(n):
    res = D[i] % m
    result[res] += 1
ans = result[0]
for i in range(m):
    a = result[i] * (result[i] - 1) // 2
    ans += a
    
print(ans)