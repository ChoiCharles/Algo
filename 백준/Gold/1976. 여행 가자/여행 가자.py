import sys
input = sys.stdin.readline

def find(a):
    if a == city[a]:
        return a
    a = find(city[a])
    return a

def union(a, b):
    fa, fb = find(a), find(b)
    if fa != fb:
        city[fb] = fa

n = int(input())
city = [0] * (n + 1)
for i in range(n + 1):
    city[i] = i
m = int(input())
for i in range(1, n + 1):
    root = list(map(int, input().split()))
    for j in range(n):
        if root[j]:
            union(i, j + 1)
tour = list(map(int, input().split()))
ans = find(tour[0])
for i in range(1, m):
    if ans != find(tour[i]):
        ans = 0
        break
if ans:
    print('YES')
else:
    print('NO')