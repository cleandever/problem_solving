"""
https://programmers.co.kr/learn/courses/30/lessons/42747
"""
def solution(citations):
    max_citation = max(citations)
    for h in range(max_citation, -1, -1):
        count = len(list(filter(lambda x: x >= h, citations)))
        if (len(citations) - count) <= h <= count:
            return h


assert solution([3, 0, 6, 1, 5]) == 3
assert solution([3, 3]) == 2
assert solution([2]) == 1
assert solution([1]) == 1
assert solution([5, 5, 1]) == 2
assert solution([5]) == 1
