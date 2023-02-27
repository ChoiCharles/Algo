import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
ver = []
hori = []
for i in range(k):
    a, b = map(int, input().split())
    if a == 0:
        hori.append((a, b))
    else:
        ver.append((a, b))
hori = list(sorted(hori, key = lambda x:x[1]))
ver = list(sorted(ver, key = lambda x:x[1]))
mh = 0
mv = 0
for i in range(1, len(hori)):
    a = hori[i][1] - hori[i - 1][1]
    if mh < a:
        mh = a
for i in range(1, len(ver)):
    a = ver[i][1] - ver[i - 1][1]
    if mv < a:
        mv = a
try:
    if mh < n - hori[-1][1]:
        mh = n - hori[-1][1]
    if mh < hori[0][1]:
        mh = hori[0][1]
except:
    pass
try:
    if mv < m - ver[-1][1]:
        mv = m - ver[-1][1]
    if mv < ver[0][1]:
        mv = ver[0][1]
except:
    pass
if mv == 0:
    mv = m
if mh == 0:
    mh = n
print(mv*mh)