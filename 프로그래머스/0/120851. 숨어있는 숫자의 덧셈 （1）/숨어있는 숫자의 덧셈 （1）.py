def solution(my_string):
    total = 0
    for ch in my_string:
        if ch.isdigit():
            total += int(ch)
    return total
