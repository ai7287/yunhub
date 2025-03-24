def solution(my_string, letter):
    answer = ''
    list_my_string = list(my_string)
    
    for i in list_my_string:
        if i != letter:
            answer+= i
        
    return answer