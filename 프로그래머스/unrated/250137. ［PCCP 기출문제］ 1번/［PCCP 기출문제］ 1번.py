def solution(bandage, health, attacks):
    answer = 0
    nowHealth = health
    flag = 0
    attack = 0
    for i in range(1, attacks[-1][0] + 1):
        if attacks[attack][0] == i:
            nowHealth -= attacks[attack][1]
            if nowHealth <= 0:
                return -1
            attack += 1
            flag = 0
        else:
            nowHealth += bandage[1]
            flag += 1
            if flag == bandage[0]:
                flag = 0
                nowHealth += bandage[2]
            if nowHealth > health:
                nowHealth = health
        
    return nowHealth