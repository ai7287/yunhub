def solution(lines):
    coords = [0] * 201  # 인덱스: -100 ~ 100 → 0 ~ 200

    for start, end in lines:
        for i in range(start, end):
            coords[i + 100] += 1
    return sum(1 for x in coords if x >= 2)