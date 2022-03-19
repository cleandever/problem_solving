"""
https://programmers.co.kr/learn/courses/30/lessons/42883
"""
from itertools import combinations

# 시간 초과 발생
# def solution(number, k):
#     pick_count = len(number) - k
#     return ''.join(sorted(list(combinations(number, pick_count)), reverse=True)[0])

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


assert solution("1924", 2) == "94"
assert solution("1231234", 3) == "3234"
assert solution("4177252841", 4) == "775841"


