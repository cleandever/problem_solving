"""
https://programmers.co.kr/learn/courses/30/lessons/12933
"""
def solution(n):
    # n을 int로 형 변환하지 않으면 TC 2/3/11 runtime 에러 발생
    n = list(str(int(n)))
    n.sort(reverse=True)
    return int("".join(n))


assert solution(8000000000) == 8000000000
assert solution(118372) == 873211
