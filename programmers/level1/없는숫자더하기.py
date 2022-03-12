"""
https://programmers.co.kr/learn/courses/30/lessons/86051
"""


def solution(numbers):
    return sum(set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(numbers))


assert solution([5, 8, 4, 0, 6, 7, 9]) == 6
