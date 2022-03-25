"""
https://programmers.co.kr/learn/courses/30/lessons/12911
"""


def solution(n):
    x = n + 1
    n_one_count = bin(n).count('1')

    while True:
        if bin(x).count('1') == n_one_count:
            return x
        x += 1


assert solution(78) == 83
assert solution(15) == 23