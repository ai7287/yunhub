def solution(numbers):
    a= max(numbers)
    numbers.pop(numbers.index(max(numbers)))
    b=max(numbers)
    return a*b