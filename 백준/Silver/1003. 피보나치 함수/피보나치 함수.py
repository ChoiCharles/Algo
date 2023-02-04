zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(n):
    l = len(zero)
    if n >= l:
        for i in range(l, n + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2]+ one [i - 1])
    print(zero[n], one[n])

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    fibo(n)