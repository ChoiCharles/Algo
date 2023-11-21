def solution(players, callings):
    dic = {name:idx for idx, name in enumerate(players)}
    answer = players
    for i in callings:
        idx = dic[i]
        answer[idx], answer[idx-1] = answer[idx-1], answer[idx]
        dic[answer[idx-1]], dic[answer[idx]] = dic[answer[idx-1]] -1, dic[answer[idx]]+1
    return answer