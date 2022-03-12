"""
https://programmers.co.kr/learn/courses/30/lessons/92334
"""
from collections import defaultdict


def solution(id_list, report, k):
    answer = []

    # 내가 신고한
    reports = defaultdict(list)

    # 나를 신고한
    reported = defaultdict(list)
    for r in report:
        id, target_id = r.split()

        # 각 유저는 한 번에 한 명의 유저를 신고
        if target_id not in reports[id]:
            reports[id].append(target_id)
            if id not in reported[target_id]:
                reported[target_id].append(id)

    for id in id_list:
        report_ids = reports[id]
        count = 0
        for report_id in report_ids:
            if len(reported[report_id]) >= k:
                count += 1
        answer.append(count)

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k = 2
assert solution(id_list, report, k) == 	[2, 1, 1, 0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
assert solution(id_list, report, k) == 	[0, 0]