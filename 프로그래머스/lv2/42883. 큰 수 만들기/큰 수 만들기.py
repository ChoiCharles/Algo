def solution(number, k):
    lst = []
    for i in number:
        while lst and k and lst[-1] < i:
            lst.pop()
            k -= 1
        lst.append(i)
    if k:
        lst = lst[:-k]
    return ''.join(lst)