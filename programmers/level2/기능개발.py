"""
https://programmers.co.kr/learn/courses/30/lessons/42586
"""
import math


def solution(progresses, speeds):
    days = [math.ceil((100-p) / float(s)) for p, s in zip(progresses, speeds)]

    # ret = []
    # pivot = 0
    # for i in range(len(days)):
    #     if days[pivot] < days[i]:
    #         ret.append(i - pivot)
    #         pivot = i
    # ret.append(len(days) - pivot)
    ret = []
    q = []
    
    return ret



assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]
