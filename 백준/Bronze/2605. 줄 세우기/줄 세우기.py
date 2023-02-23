import sys
input = sys.stdin.readline

n = int(input())
lst = []
a = list(map(int, input().split()))
j = 1
for i in a:
    if i == 0:
        lst.append(j)
    else:
        lst.insert(-i, j)
    j += 1
print(*lst)