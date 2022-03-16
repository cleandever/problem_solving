"""
https://programmers.co.kr/learn/courses/30/lessons/42746
"""
def solution(numbers):
    numbers_str = list(map(str, numbers))
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers_str)))


assert solution([6, 10, 2]) == 	"6210"
assert solution([3, 30, 34, 5, 9]) == "9534330"