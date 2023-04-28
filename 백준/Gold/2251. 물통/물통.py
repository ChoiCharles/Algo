from collections import deque

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[0 for j in range(201)] for i in range(201)]
answer = [0] * 201

def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    answer[now[2]] = 1
    while q:
        now_node = q.popleft()
        a, b = now_node[0], now_node[1]
        c = now[2] - a - b
        for k in range(6):
            next = [a, b, c]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > now[receiver[k]]:
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = 1
                q.append((next[0], next[1]))
                if next[0] == 0:
                    answer[next[2]] = 1
bfs()
for i in range(len(answer)):
    if answer[i]:
        print(i, end = ' ')