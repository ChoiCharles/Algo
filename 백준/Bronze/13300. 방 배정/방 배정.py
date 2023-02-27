import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = [0] * 13
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        lst[b] += 1
    else:
        lst[b+6] += 1
cnt = 0
for i in range(1, 13):
    a = lst[i] // k
    b = lst[i] % k
    cnt += a
    if b != 0:
        cnt += 1
print(cnt)