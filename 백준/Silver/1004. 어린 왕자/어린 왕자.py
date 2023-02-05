T = int(input())
for test_case in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for i in range(n):
        x3, y3, r = map(int, input().split())
        d1 = ((x1 - x3)**2 + (y1 - y3)**2)**0.5
        d2 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
        if d1 < r and d2 > r:
            cnt += 1
        elif d1 > r and d2 < r:
            cnt += 1
    print(cnt)