"""
https://programmers.co.kr/learn/courses/30/lessons/12915
"""


class String:
    def __init__(self, val, cmp_idx):
        self.val = val
        self.cmp_idx = cmp_idx

    def __lt__(self, other):
        if self.val[self.cmp_idx] < other.val[other.cmp_idx]:
            return True
        elif self.val[self.cmp_idx] > other.val[other.cmp_idx]:
            return False
        else:
            # 인덱스 cmp_idx 문자가 같은 문자열이 여럿 일 경우,
            # 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
            return self.val < other.val


def solution(strings, n):
    strings = [String(s, n) for s in strings]
    return [s.val for s in sorted(strings)]


assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]
