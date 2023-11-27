def solution(n, m, section):
    answer = 0
    sec = len(section) - 1
    left = 0
    right = 1
    
    while 1:
        if left > sec:
            break
        elif left >= sec:
            answer += 1
            break
        if right > sec:
            answer += 1
            break
        
        if section[right] - section[left] > m - 1:
            answer += 1
            left = right
            right += 1
        elif section[right] - section[left] == m - 1:
            answer += 1
            left = right + 1
            right = left + 1
        else:
            right += 1
        
    return answer