"""
https://programmers.co.kr/learn/courses/30/lessons/12926
"""


def solution(s, n):
    # 알파벳 매핑 테이블 생성
    lower_alphabets = 'abcdefghijklmnopqrstuvwxyz'
    upper_alphabets = lower_alphabets.upper()
    len_alphabet = len(lower_alphabets)

    lower_alphabets = [[c, i+n] for i, c in enumerate(lower_alphabets)]
    upper_alphabets = [[c, i+n] for i, c in enumerate(upper_alphabets)]

    res = []
    for c in s:
        if c == ' ':
            res.append(' ')
            continue

        if 'a' <= c <= 'z':
            alphabets = lower_alphabets
            char_idx = ord(c) - ord('a')
        else:
            alphabets = upper_alphabets
            char_idx = ord(c) - ord('A')

        next_char = alphabets[alphabets[char_idx][1] % len_alphabet]
        res.append(next_char[0])

    return ''.join(res)




assert solution('AB', 1) == 'BC'
assert solution('z', 1) == 'a'
assert solution('a B z', 4) == 'e F d'