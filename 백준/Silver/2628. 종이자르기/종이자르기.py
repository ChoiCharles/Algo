import sys
input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
ver = [0]
hori = [0]
for i in range(k):
    a, b = map(int, input().split())
    if a == 0:
        hori.append(b)
    else:
        ver.append(b)
hori.sort()
ver.sort()
hori.append(n)
ver.append(m)
mh = 0
mv = 0
for i in range(1, len(hori)):
    if mh < hori[i] - hori[i - 1]:
        mh = hori[i] - hori[i - 1]
for i in range(1, len(ver)):
    if mv < ver[i] - ver[i - 1]:
        mv = ver[i] - ver[i - 1]
print(mh * mv)