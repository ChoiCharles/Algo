a = int(input())
b = int(input())
c = int(input())
d = a * b * c
dic = {}
for i in str(d):
    if dic.get(i, 0):
        dic[i] += 1
    else:
        dic[i] = 1
for i in range(10):
    a = dic.get(str(i), 0)
    print(a)