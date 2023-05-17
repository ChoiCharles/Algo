import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    a, b = input().split()
    a = int(a)
    b = list(b)
    for j in b:
        print(j*a, end = '')
    print()