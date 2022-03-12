"""
https://programmers.co.kr/learn/courses/30/lessons/76501
"""


def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num

    return answer

assert solution([4, 7, 12], [True, False, True]) == 9