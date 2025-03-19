def gcd(n,m=6):
    if n%m==0:
        return m
    else:
        return gcd(m, n%m)
    
def solution(n):
    m=6
    if n%6 ==0:
        answer = n/6
    else:
        answer = (n*m // gcd(m,n))/6
    return answer