def find():
    count = 0
    for i in range(n):
        while 1:
            idx = lst.index(i)
            cnt = bigger(i, idx)
            a = lst2[i] - cnt
            if a == 0:
                break
            count += 1
            sort(idx, a)
    return count

def bigger(a, idx):
    cnt = 0
    for i in range(idx, -1, -1):
        if lst[i] > a:
            cnt += 1
    return cnt

def sort(idx, cnt):
    if cnt > 0:
        i = 0
        while cnt > i:
            lst[idx], lst[idx+1] = lst[idx+1], lst[idx]
            idx += 1
            i += 1
    elif cnt < 0:
        i = 0
        while cnt > i:
            lst[idx], lst[idx - 1] = lst[idx-1], lst[idx]
            idx -= 1
            i += 1

n = int(input())
lst = []
for i in range(n):
    lst.append(i)
lst2 = list(map(int, input().split()))

while 1:
    count = find()
    if count == 0:
        break

for i in lst:
    print(i + 1, end = ' ')