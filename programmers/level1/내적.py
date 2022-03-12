"""
https://programmers.co.kr/learn/courses/30/lessons/70128
"""


def solution(a, b):
    return sum([n1*n2 for n1, n2 in zip(a, b)])