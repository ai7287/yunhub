def solution(my_string):
    # 1. 모든 문자를 소문자로 변환
    my_string = my_string.lower()
    
    # 2. 문자열을 리스트로 변환하여 정렬
    sorted_chars = sorted(my_string)
    
    # 3. 정렬된 문자 리스트를 문자열로 다시 결합
    return ''.join(sorted_chars)
