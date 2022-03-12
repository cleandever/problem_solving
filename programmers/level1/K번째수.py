"""
https://programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sub_array = array[i - 1:j]
        sub_array = sorted(sub_array)
        answer.append(sub_array[k - 1])

    return answer


assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5,6,3]