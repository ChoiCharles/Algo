import sys
import copy
input = sys.stdin.readline


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
MAX = 0

def asdf(a, l = 0):
    idx = arr[l].index(a)
    if idx == 0:
        b = 5
    elif idx == 1 or idx == 2:
        b = idx + 2
    elif idx == 3 or idx == 4:
        b = idx - 2
    elif idx == 5:
        b = 0
    c = arr[l][b]
    lst = copy.deepcopy(arr[l])
    lst.remove(a)
    lst.remove(c)
    M = max(lst)
    return M, c
for i in arr[0]:
    sum = 0
    c = i
    for j in range(n):
        a, c = asdf(c, j)
        sum += a
    if sum > MAX:
        MAX = sum
print(MAX)