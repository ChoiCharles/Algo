import sys
input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key = lambda x:(x[1], x[0]))
end = lst[0][1]
cnt = 1
for i in range(1, n):
    a, b = lst[i]
    if a < end:
        continue
    else:
        cnt += 1
        end = b
print(cnt)