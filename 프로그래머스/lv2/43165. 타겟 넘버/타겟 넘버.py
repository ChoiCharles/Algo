def solution(numbers, target):
    answer = 0
    l = len(numbers)
    
    def dfs(idx, num, l, target):
        if idx == l:
            if num == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, num + numbers[idx], l, target)
        dfs(idx + 1, num - numbers[idx], l, target)
        
    dfs(0, 0, l, target)
    return answer