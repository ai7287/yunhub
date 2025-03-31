def solution(n):
    def is_composite(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return True
        return False

    count = 0
    for i in range(1, n + 1):
        if is_composite(i):
            count += 1
    return count
