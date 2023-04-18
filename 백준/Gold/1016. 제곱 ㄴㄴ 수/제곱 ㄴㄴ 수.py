import math

MIN, MAX = map(int, input().split())
lst = [0] * (MAX-MIN+1)
for i in range(2, int(math.sqrt(MAX))+1):
    a = i*i
    s = int(MIN/a)
    if MIN % a:
        s += 1
    for j in range(s, int(MAX/a)+1):
        lst[int(j*a)-MIN] = 1
cnt = 0
for i in (lst):
    if not i:
        cnt += 1
print(cnt)