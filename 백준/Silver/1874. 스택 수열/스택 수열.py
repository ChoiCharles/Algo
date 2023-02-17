import sys
input = sys.stdin.readline


n = int(input())
ans = []
k = 0
lst = []
flag = 0
for i in range(n):
    a = int(input())

    while a > k:
        k += 1
        lst.append(k)
        ans.append('+')
    b = lst.pop()
    if a == b:
        ans.append('-')
    else:
        flag += 1
        break
if flag > 0:
    print('NO')
else:
    for i in ans:
        print(i)