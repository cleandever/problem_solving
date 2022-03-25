"""
https://programmers.co.kr/learn/courses/30/lessons/72411
"""
from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    ret = []

    # 단품메뉴 조합을 정렬
    orders = [sorted(order) for order in orders]

    for num in course:
        d = defaultdict(int)
        for order in orders:
            for menu in list(combinations(order, num)):
                d[menu] += 1

        max_count = 0
        count_d = defaultdict(list)
        for menu, count in d.items():
            count_d[count].append(menu)
            if max_count <= count:
                max_count = count

        # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합
        if max_count > 1:
            ret += [''.join(menu) for menu in count_d[max_count]]

    return sorted(ret)


assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) == ["AC", "ACDE", "BCFG", "CDE"]
assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]
assert solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"]
