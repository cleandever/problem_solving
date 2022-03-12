"""
https://programmers.co.kr/learn/courses/30/lessons/67256
"""


def solution(numbers, hand):
    # 손가락 초기 위치
    lh_pos = '*'
    rh_pos = '#'

    # 키패드 위치를 row, column 표현
    points = {
        1:   [0, 0],   2: [0, 1],   3: [0, 2],
        4:   [1, 0],   5: [1, 1],   6: [1, 2],
        7:   [2, 0],   8: [2, 1],   9: [2, 2],
        '*': [3, 0],   0: [3, 1], '#': [3, 2]
    }

    res = []
    for n in numbers:
        if n in [1, 4, 7]:
            res.append('L')
            lh_pos = n
        elif n in [3, 6, 9]:
            res.append('R')
            rh_pos = n
        else:
            # 거리 측정
            lh_distance = get_distance(points[lh_pos], points[n])
            rh_distance = get_distance(points[rh_pos], points[n])

            if lh_distance < rh_distance:
                res.append('L')
                lh_pos = n
            elif lh_distance > rh_distance:
                res.append('R')
                rh_pos = n
            else:
                # 거리가 동일
                if hand == 'left':
                    res.append('L')
                    lh_pos = n
                else:
                    res.append('R')
                    rh_pos = n

    return ''.join(res)


# 거리 계산
def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


nums = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'
assert solution(nums, hand) == "LRLLLRLLRRL"

nums = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = 'left'
assert solution(nums, hand) == "LRLLRRLLLRR"

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'
assert solution(nums, hand) == "LLRLLRLLRL"
