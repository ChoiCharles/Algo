lst = list(map(int, input()))
lst.sort(reverse=True)
print(*lst, sep='')