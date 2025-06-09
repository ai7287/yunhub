def solution(polynomial):
    terms = polynomial.split(' + ')
    x_sum = 0
    num_sum = 0
    
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_sum += 1
            else:
                x_sum += int(term.replace('x', ''))
        else:
            num_sum += int(term)
    
    result = []
    if x_sum:
        result.append(f"{x_sum}x" if x_sum > 1 else "x")
    if num_sum:
        result.append(str(num_sum))
    
    return ' + '.join(result)
