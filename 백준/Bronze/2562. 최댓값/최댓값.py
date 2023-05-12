import sys
input = sys.stdin.readline

MAX = 0
idx = 0
for i in range(1, 10):
    a = int(input())
    if a > MAX:
        MAX = a
        idx = i
print(MAX)
print(idx)