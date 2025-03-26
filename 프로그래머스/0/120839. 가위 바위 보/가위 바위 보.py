def solution(rsp):
    result={'2':'0','5':'2','0':'5'}
    answer=''
    for i in rsp:
        answer+=result.get(i)
    return answer