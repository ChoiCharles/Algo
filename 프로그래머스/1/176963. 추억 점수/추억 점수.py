def solution(name, yearning, photo):
    answer = [0] * len(photo)
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            try:
                idx = name.index(photo[i][j])
                answer[i] += yearning[idx]
            except:
                continue
            
    return answer