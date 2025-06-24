def solution(score):
    avg_with_index = [(sum(s)/2, i) for i, s in enumerate(score)]
    sorted_avg = sorted(avg_with_index, key=lambda x: -x[0])

    ranks = [0] * len(score)
    current_rank = 1
    for i in range(len(sorted_avg)):
        if i > 0 and sorted_avg[i][0] == sorted_avg[i - 1][0]:
            rank = current_rank
        else:
            rank = i + 1
            current_rank = rank
        ranks[sorted_avg[i][1]] = rank

    return ranks
