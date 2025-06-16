def solution(dots):
    from itertools import combinations

    for (a1, a2), (b1, b2) in combinations(combinations(dots, 2), 2):
        if len({tuple(a1), tuple(a2), tuple(b1), tuple(b2)}) < 4:
            continue
        if (a2[1] - a1[1]) * (b2[0] - b1[0]) == (b2[1] - b1[1]) * (a2[0] - a1[0]):
            return 1
    return 0
