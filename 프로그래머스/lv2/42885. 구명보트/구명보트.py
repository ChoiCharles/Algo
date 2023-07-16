def solution(people, limit):
    people.sort()
    answer = 0
    n = len(people)
    left = 0
    right = n - 1
    answer = 0
    while left <= right:
        now = people[right]
        right -= 1
        answer += 1
        while now <= limit:
            if people[left] + now > limit:
                break
            left += 1
            now += people[left]
    return answer