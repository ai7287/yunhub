def solution(n):
    answer = int(n/7)
    if(n%7 != 0):
        answer +=1
    return answer