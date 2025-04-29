def solution(my_string):
    num = 0
    answer = 0
    sign = 1

    for ch in my_string:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '+':
            answer += sign * num
            num = 0
            sign = 1
        elif ch == '-':
            answer += sign * num
            num = 0
            sign = -1
        elif ch == ' ':
            continue

    answer += sign * num
    return answer
