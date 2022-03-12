"""
https://programmers.co.kr/learn/courses/30/lessons/12950
"""
import operator


def solution(arr1, arr2):
    res = []
    for row1, row2 in zip(arr1, arr2):
        res.append(list(map(operator.add, row1, row2)))
    return res


assert solution([[1,2],[2,3]], [[3,4],[5,6]]) == [[4,6],[7,9]]