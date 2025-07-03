def solution(i, j, k):
    count = 0
    k_str = str(k)
    for num in range(i, j + 1):
        count += str(num).count(k_str)
    return count
