def isprime(a):
    for i in range(2, int((a-1)/2)):
        if a % i == 0:
            return False
    return True

def dfs(a):
    if len(path) == n:
        print(a)
        return
    for i in ('1', '3', '5', '7', '9'):
        path.append(i)
        num = int(''.join(path))
        if num % 2 == 0:
            continue
        if isprime(num):
            dfs(num)
        path.pop()

n = int(input())
for i in ('2', '3', '5', '7'):
    path = [i]
    dfs(i)