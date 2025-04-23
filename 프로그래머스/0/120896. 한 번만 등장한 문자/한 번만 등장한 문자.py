def solution(s):
    count_dict = {}
    for char in s:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    result = []
    for char in count_dict:
        if count_dict[char] == 1:
            result.append(char)
    result.sort()
    return ''.join(result)
