def solution(board, h, w):
    n = len(board)
    answer = 0
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = h + di, w + dj
        if 0 <= ni < n and 0 <= nj < n:
            if board[h][w] == board[ni][nj]:
                answer += 1
    return answer