"""
https://programmers.co.kr/learn/courses/30/lessons/12899
"""
def solution(n):
    ret = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        if remainder == 1:
            ret = '1' + ret
        elif remainder == 2:
            ret = '2' + ret
        else:
            ret = '4' + ret
            n -= 1
    return ret


assert solution(10) == '41'
