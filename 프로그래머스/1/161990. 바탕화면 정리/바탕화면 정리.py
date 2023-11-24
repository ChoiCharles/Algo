def transparent(arr, n, m):
    trans = [[0]*n for i in range(m)]
    for i in range(n):
        for j in range(m):
            trans[j][i] = arr[i][j]
    return trans

def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    answer = [0, 0, n-1, m-1]
    flag = 1
    while 1:
        if flag:
            for i in wallpaper[answer[0]]:
                if i == '#':
                    flag = 0
                    break
            answer[0] += 1
        else:
            break
    flag = 1
    while 1:
        if flag:
            for i in wallpaper[answer[2]]:
                if i == '#':
                    flag = 0
                    break
            answer[2] -= 1
        else:
            break
    wallpaper = transparent(wallpaper, n, m)
    flag = 1
    while 1:
        if flag:
            for i in wallpaper[answer[1]]:
                if i == '#':
                    flag = 0
                    break
            answer[1] += 1
        else:
            break
    flag = 1
    while 1:
        if flag:
            for i in wallpaper[answer[3]]:
                if i == '#':
                    flag = 0
                    break
            answer[3] -= 1
        else:
            break
    
    answer[0] -= 1
    answer[1] -= 1
    answer[2] += 2
    answer[3] += 2
    
    return answer