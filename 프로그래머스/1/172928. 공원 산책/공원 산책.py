def solution(park, routes):
    y, x = 0, 0
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                y, x = i, j

    for st in routes:
        flag = 0
        route = list(st)
        if route[0] == 'N':
            ny = y
            nx = x
            for i in range(1, int(route[2]) + 1):
                ny -= 1
                if 0 <= ny < len(park):
                    if park[ny][nx] == 'X':
                        flag = 1
                        break
                else:
                    flag = 1
            if flag == 0:
                y, x = ny, nx
        elif route[0] == 'S':
            ny = y
            nx = x
            for i in range(1, int(route[2]) + 1):
                ny += 1
                if 0 <= ny < len(park):
                    if park[ny][nx] == 'X':
                        flag = 1
                        break
                else:
                    flag = 1
            if flag == 0:
                y, x = ny, nx
        elif route[0] == 'W':
            nx = x
            ny = y
            for i in range(1, int(route[2]) + 1):
                nx -= 1
                if 0 <= nx < len(park[0]):
                    if park[ny][nx] == 'X':
                        flag = 1
                        break
                else:
                    flag = 1
            if flag == 0:
                y, x = ny, nx
        elif route[0] == 'E':
            nx = x
            ny = y
            for i in range(1, int(route[2]) + 1):
                nx += 1
                if 0 <= nx < len(park[0]):
                    if park[ny][nx] == 'X':
                        flag = 1
                        break
                else:
                    flag = 1
            if flag == 0:
                y, x = ny, nx
    answer = [y, x]
    return answer