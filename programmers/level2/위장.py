"""
https://programmers.co.kr/learn/courses/30/lessons/42578
"""
import operator
from functools import reduce
from collections import defaultdict


def solution(clothes):
    d = defaultdict(list)
    for clothes_name, clothes_type in clothes:
        d[tuple(clothes_type)].append(clothes_name)
    return reduce(operator.mul, [len(v)+1 for v in d.values()]) - 1


assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5