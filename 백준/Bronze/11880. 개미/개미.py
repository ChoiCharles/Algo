import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    lst = list(map(int, input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    c = lst[2]
    print((a + b) ** 2 + (c ** 2))