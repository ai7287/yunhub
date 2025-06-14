def solution(spell, dic):
    spell_str = ''.join(sorted(spell))
    for word in dic:
        if ''.join(sorted(word)) == spell_str:
            return 1
    return 2
