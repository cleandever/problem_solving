"""
https://programmers.co.kr/learn/courses/30/lessons/42587
"""
from collections import deque


def solution(priorities, location):
    p = deque([(p, i) for i, p in enumerate(priorities)])

    ret = []
    while p:
        max_p = max(list(zip(*p))[0])
        if p[0][0] >= max_p:
            ret.append(p.popleft())
            if location == ret[-1][1]:
                return len(ret)
        else:
            p.append(p.popleft())


assert solution([2, 1, 3, 2], 2) == 1
assert solution([1, 1, 9, 1, 1, 1], 0) == 5