def factorial(a):
    if(a>1):
        return a*factorial(a-1)
    else:
        return 1
    
def solution(balls, share):
    answer = factorial(balls)/(factorial(balls-share)*factorial(share))
    return answer