"""
https://programmers.co.kr/learn/courses/30/lessons/12912
"""


def solution(a, b):
    nums = sorted([a, b])
    return sum(range(nums[0], nums[1]+1))