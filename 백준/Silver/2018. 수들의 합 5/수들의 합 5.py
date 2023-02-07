import sys
input = sys.stdin.readline

n = int(input())
cnt = 1
sum = 1
si = 1
ei = 1
while ei != n:
    if sum == n:
        cnt += 1
        ei += 1
        sum += ei
    elif sum > n:
        sum -= si
        si += 1
    elif sum < n:
        ei += 1
        sum += ei
print(cnt)