"""
https://programmers.co.kr/learn/courses/30/lessons/60057
"""


def split_string_by_n(s, n):
    words = []

    # n개 단위로 자르기
    start = 0
    while (start + n) < len(s):
        words.append(s[start:start + n])
        start += n

    # 마지막에 남는 문자열은 그대로 붙이기
    words.append(s[start:])

    return words


def solution(s):
    if len(s) == 1:
        return 1

    lengths = []
    for i in range(1, len(s) // 2 + 1):
        words = split_string_by_n(s, i)

        zip_words = []
        pivot = 0
        for j in range(1, len(words)):
            if words[pivot] != words[j]:
                count = j - pivot
                count = '' if count == 1 else count
                zip_words.append(f'{count}{words[pivot]}')
                pivot = j

        count = len(words) - pivot
        count = '' if count == 1 else count
        zip_words.append(f'{count}{words[pivot]}')

        lengths.append(len(''.join(zip_words)))

    return min(lengths)


assert solution("aabbaccc") == 7
assert solution("a") == 1
assert solution("aa") == 2