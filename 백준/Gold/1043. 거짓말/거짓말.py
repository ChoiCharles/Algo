import sys
input = sys.stdin.readline

def find(a):
    if a == people[a][0]:
        return a
    a = find(people[a][0])
    return a

def union(a, b):
    fa, fb = find(a), find(b)
    if fa != fb:
        people[fb][0] = fa

n, m = map(int, input().split())
tru = list(map(int, input().split()))
people = [[0] for _ in range(n + 1)]
for i in range(n + 1):
    people[i][0] = i
if tru[0] == 0:
    print(m)
else:
    for i in range(m):
        mem = list(map(int, input().split()))
        people[mem[1]].append(i + 1)
        for j in range(mem[0] - 1):
            union(mem[1], mem[j + 2])
            people[mem[j + 2]].append(i + 1)
    truth = []
    for i in range(1, tru[0] + 1):
        truth.append(find(tru[i]))
    res = []
    for i in range(1, n + 1):
        if find(people[i][0]) not in truth:
            res.append(i)
    ans = []
    for i in res:
        l = len(people[i])
        for j in range(1, l):
            if people[i][j] not in ans:
                ans.append(people[i][j])
    print(len(ans))