def solution(n, numlist):
    answer=[]
    for a in numlist:
        if a%n==0:
            answer.append(a)
    return answer