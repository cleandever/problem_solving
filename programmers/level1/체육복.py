"""
https://techblog-history-younghunjo1.tistory.com/451
"""


def solution(n, lost, reserve):
    # 도난 당했는데 여벌옷 있는 사람은 미리 제거
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for i in new_reserve:
        if i - 1 in new_lost:
            new_lost.remove(i - 1)
        elif i + 1 in new_lost:
            new_lost.remove(i + 1)
    return n - len(new_lost)


assert solution(5, [2, 4], [1, 3, 5]) == 5
assert solution(5, [2, 4], [3]) == 4
