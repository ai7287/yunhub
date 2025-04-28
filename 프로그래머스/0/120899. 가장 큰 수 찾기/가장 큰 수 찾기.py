def solution(array):
    max_value = max(array)       # 가장 큰 수를 찾음
    max_index = array.index(max_value)  # 그 수의 인덱스를 찾음
    return [max_value, max_index]
