"""
https://programmers.co.kr/learn/courses/30/lessons/17680
"""
from collections import deque
def solution(cacheSize, cities):
    runtime = 0
    cache = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in cache:
            cache.remove(city)
            cache.append(city)
            runtime += 1
        else:
            cache.append(city)
            runtime += 5
    return runtime


assert solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 50
assert solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]) == 21
assert solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 60
assert solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]) == 52
assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
assert solution(30, ['a', 'a', 'a']) == 7
