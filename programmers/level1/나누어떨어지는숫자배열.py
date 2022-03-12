"""
https://programmers.co.kr/learn/courses/30/lessons/12910
"""


def solution(arr, divisor):
    ret = sorted([n for n in arr if n % divisor == 0])
    return ret if ret else [-1]