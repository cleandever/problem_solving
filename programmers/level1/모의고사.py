"""
https://programmers.co.kr/learn/courses/30/lessons/42840
"""


def solution(answers):
    s1 = [1, 2, 3, 4, 5] * 2000
    s2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000

    s1_count = 0
    s2_count = 0
    s3_count = 0
    for i in range(len(answers)):
        if answers[i] == s1[i]:
            s1_count += 1
        if answers[i] == s2[i]:
            s2_count += 1
        if answers[i] == s3[i]:
            s3_count += 1

    max_count = max(s1_count, s2_count, s3_count)
    answers = [(s1_count, 1), (s2_count, 2), (s3_count, 3)]
    answers = sorted(answers, key=lambda x: (x[0], -x[1]), reverse=True)

    return [answer[1] for answer in answers if answer[0] == max_count]


assert solution([1,2,3,4,5]	) == [1]
assert solution([1,3,2,4,2]	) == [1, 2, 3]