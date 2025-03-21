def solution(my_string, n):
    answer = ''
    my_string_list = list(my_string)
    for i in my_string_list:
        answer += i*n
    return answer