def solution(n):
    answer = 1
    i = 1
    while answer * (i + 1) <= n:
        i += 1
        answer *= i
    return i

