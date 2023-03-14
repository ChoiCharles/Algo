import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [-1] * n
stack.append(0)
for i in range(1, n):
    while stack and lst[stack[-1]] < lst[i]:
        ans[stack.pop()] = lst[i]
    stack.append(i)
print(*ans)