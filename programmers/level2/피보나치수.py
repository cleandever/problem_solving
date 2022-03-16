"""
https://programmers.co.kr/learn/courses/30/lessons/12945
"""
def solution(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[-2]+fibo[-1])
    return fibo[n] % 1234567


assert solution(3) == 2
assert solution(5) == 5