import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(1, n):
        a[j] += a[j - 1]
    a.insert(0, 0)
    arr.append(a)
for i in range(m):
    result = 0
    y1, x1, y2, x2 = map(int, input().split())
    for j in range(y1-1, y2):
        result += arr[j][x2] - arr[j][x1 - 1]
    print(result)