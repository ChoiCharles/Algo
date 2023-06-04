dic = {}
for i in range(10):
    a = int(input())
    b = a % 42
    if dic.get(b, 0):
        dic[b] += 1
    else:
        dic[b] = 1
print(len(dic))