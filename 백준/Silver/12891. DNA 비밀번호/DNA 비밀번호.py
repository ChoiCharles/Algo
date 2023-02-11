import sys
input = sys.stdin.readline

s, p = map(int, input().split())
st = list(input())
check = list(map(int, input().split()))

pw = [0] * 4
cnt = 0
result = 0

def add(a):
    global cnt
    if a == 'A':
        pw[0] += 1
        if check[0] == pw[0]:
            cnt += 1
    elif a == 'C':
        pw[1] += 1
        if check[1] == pw[1]:
            cnt += 1
    elif a == 'G':
        pw[2] += 1
        if check[2] == pw[2]:
            cnt += 1
    elif a == 'T':
        pw[3] += 1
        if check[3] == pw[3]:
            cnt += 1

def remove(a):
    global cnt
    if a == 'A':
        if check[0] == pw[0]:
            cnt -= 1
        pw[0] -= 1
    elif a == 'C':
        if check[1] == pw[1]:
            cnt -= 1
        pw[1] -= 1
    elif a == 'G':
        if check[2] == pw[2]:
            cnt -= 1
        pw[2] -= 1
    elif a == 'T':
        if check[3] == pw[3]:
            cnt -= 1
        pw[3] -= 1

for i in check:
    if i == 0:
        cnt += 1

for i in range(p):
    add(st[i])
if cnt == 4:
    result += 1

for i in range(p, s):
    j = i - p
    add(st[i])
    remove(st[j])
    if cnt == 4:
        result += 1
print(result)