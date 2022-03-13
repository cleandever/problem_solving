"""
https://programmers.co.kr/learn/courses/30/lessons/12954
"""


def solution1(x, n):
    res = []
    cur = x
    while n > 0:
        res.append(cur)
        cur += x
        n -= 1
    return res


def solution2(x, n):
    return [x + (i*x) for i in range(n)]


assert solution2(2, 5) == [2,4,6,8,10]
assert solution2(-4, 2) == [-4, -8]