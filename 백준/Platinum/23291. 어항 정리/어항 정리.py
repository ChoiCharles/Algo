def rotatequarterccw(arr):
    n = len(arr)
    m = len(arr[0])
    res = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            res[m-j-1][i] = arr[i][j]
    return res

def rotatehalf(arr):
    n = len(arr)
    try:
        m = len(arr[0])
        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res[n - i - 1][m - j - 1] = arr[i][j]
    except:
        m = 1
        res = [0] * n
        for i in range(n):
            res[n - i - 1] = arr[i]
    return res

def plus_fish(lst):
    MIN = lst[0]
    for i in range(1, N):
        MIN = min(MIN, lst[i])
    for i in range(N):
        if lst[i] == MIN:
            lst[i] += 1

def met_one(arr):
    a = arr[0].pop(0)
    arr.append([a])
    base = N - 1
    ver_len = 2
    hor_len = 1
    flag = 1
    while 1:
        if base - hor_len < ver_len and flag != 1:
            break
        temp_arr = [[0] * hor_len for _ in range(ver_len)]
        for i in range(ver_len):
            for j in range(hor_len):
                a = arr[i].pop(0)
                temp_arr[i][j] = a
        temp_arr = rotatequarterccw(temp_arr)
        arr = [arr[0]] + temp_arr
        base -= hor_len
        if flag % 2:
            hor_len += 1
        else:
            ver_len += 1
        flag += 1
    return arr

def after_met_one(arr):
    lst = []
    len_y = len(arr)
    len_x = len(arr[0])
    for j in range(len_x):
        for i in range(len_y):
            if arr[i][j]:
                lst.append(arr[i][j])
    return lst

def met_two(lst):
    arr = [lst[N//2:]] + [rotatehalf(lst[:N//2])]
    half = []
    rem = []
    for i in range(2):
        half += [arr[i][:N//4]]
        rem += [arr[i][N//4:]]
    res = rem + rotatehalf(half)
    return res

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))
def adjust_fish(arr):
    len_y = len(arr)
    len_x = len(arr[0])
    calc_arr = [[0]*len_x for _ in range(len_y)]
    res_arr = [[0]*len_x for _ in range(len_y)]
    for i in range(len_y):
        for j in range(len_x):
            try:
                calc_arr[i][j] = arr[i][j]
                res_arr[i][j] = arr[i][j]
            except:
                pass
    for i in range(len_y):
        for j in range(len_x):
            for dy, dx in dir:
                ny, nx = i + dy, j + dx
                if calc_arr[i][j] != 0:
                    if 0 <= ny < len_y and 0 <= nx < len_x and calc_arr[ny][nx] != 0:
                        r = (calc_arr[ny][nx] - calc_arr[i][j]) // 5
                        if r >= 1:
                            res_arr[ny][nx] -= r
                            res_arr[i][j] += r
    return res_arr

N, k = map(int, input().split())
lst = list(map(int, input().split()))
z = 1
while 1:
    plus_fish(lst)
    arr = met_one([lst])
    arr = adjust_fish(arr)
    lst = after_met_one(arr)
    arr = met_two(lst)
    arr = adjust_fish(arr)
    lst = after_met_one(arr)
    ans = max(lst) - min(lst)
    if ans <= k:
        break
    z += 1
print(z)