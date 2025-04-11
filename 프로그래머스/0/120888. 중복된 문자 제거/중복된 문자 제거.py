def solution(my_string):
    result = ''
    seen = set()
    for ch in my_string:
        if ch not in seen:
            result += ch
            seen.add(ch)
    return result
