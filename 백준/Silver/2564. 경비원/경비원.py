import sys
input = sys.stdin.readline

j, i = map(int, input().split())
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
y, x = map(int, input().split())
sum = 0
for k in lst:
    a, b = k[0], k[1]
    if y == 1:
        if a == 3:
            sum += x + b
        elif a == 4:
            sum += j - x + b
        elif a == 1:
            sum += abs(b - x)
        else:
            if (x + b) / 2 > (j / 2):
                sum += i + 2 * j - x - b
            else:
                sum += i + x + b
    elif y == 2:
        if a == 3:
            sum += x + (i - b)
        elif a == 4:
            sum += j - x + i - b
        elif a == 2:
            sum += abs(b - x)
        else:
            if (x + b) / 2 > (j / 2):
                sum += i + 2 * j - x - b
            else:
                sum += i + x + b
    elif y == 3:
        if a == 1:
            sum += x + b
        elif a == 2:
            sum += i - x + b
        elif a == 3:
            sum += abs(b - x)
        else:
            if (x + b) / 2 > (i / 2):
                sum += j + 2 * i - x - b
            else:
                sum += j + x + b
    elif y == 4:
        if a == 1:
            sum += j - b + x
        elif a == 2:
            sum += i - x + j - b
        elif a == 4:
            sum += abs(b - x)
        else:
            if (x + b) / 2 > (i / 2):
                sum += j + 2 * i - x - b
            else:
                sum += j + x + b
print(sum)