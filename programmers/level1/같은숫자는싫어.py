"""
https://programmers.co.kr/learn/courses/30/lessons/12906
"""


def solution(arr):
    res = []
    start = 0
    for i in range(1, len(arr)):
        if arr[start] != arr[i]:
            res.append(arr[start])
            start = i
    res.append(arr[start])
    return res


assert solution([1,1,3,3,0,1,1]	) == [1,3,0,1]
assert solution([1,1,1,1,1]) == [1]
assert solution([1,1,2 ]) == [1, 2]