import sys
input = sys.stdin.readline

def asdf(lst):
    res = 0
    for i in range(1, n+1):
        res += sum(lst[:i])
    return res

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = asdf(lst)
print(ans)