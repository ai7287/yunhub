def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    count = 0

    for b in babbling:
        temp = b
        for w in words:
            if w in temp:
                temp = temp.replace(w, ' ', 1)
        if temp.replace(' ', '') == '':
            count += 1

    return count
