"""
https://programmers.co.kr/learn/courses/30/lessons/17682
"""
from functools import reduce
import operator
def solution(dartResult):
    idx = 0
    nums = []
    squares = {'S': 1, 'D': 2, 'T': 3}
    ret = [[], [], []]

    for c in dartResult:
        if c.isdigit():
            nums.append(c)
        elif c.isalpha():
            num = int(''.join(nums))
            ret[idx].append(num ** squares[c])
            idx += 1
            nums.clear()
        else:
            if c == '*':
                ret[idx - 1].append(2)
                if idx - 2 >= 0:
                    ret[idx - 2].append(2)
            elif c == '#':
                ret[idx-1].append(-1)

    return sum([reduce(operator.mul, r) for r in ret])


assert solution("1S*2T*3S") == 23
assert solution("1D#2S*3S") == 5