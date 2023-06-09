n = int(input())
vote = int(input())
lst = list(input().split())
dic = {}
num = 0
length = 0
for i in lst:
    num += 1
    if dic.get(i, 0):
        dic[i][0] += 1
    else:
        if length < n:
            dic[i] = [1, num]
            length += 1
        else:
            dic_sort = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
            for key, value in enumerate(dic_sort):
                a = value
            del dic[a[0]]
            dic[i] = [1, num]
res = sorted(dic, key=lambda x: int(x))
print(*res)