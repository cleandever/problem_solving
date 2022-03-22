"""
https://programmers.co.kr/learn/courses/30/lessons/17677
"""
import re
from collections import Counter


def solution(str1, str2):
    # 대문자와 소문자의 차이는 무시
    str1, str2 = str1.lower(), str2.lower()

    str1 = re.findall('[a-z]+', str1)
    str2 = re.findall('[a-z]+', str2)

    words1 = [split_by_2chars(s) for s in str1]
    words2 = [split_by_2chars(s) for s in str2]

    # list to 1-dimension
    words1 = sum(words1, [])
    words2 = sum(words2, [])

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    intersection_count = get_intersection_count(counter1, counter2)
    union_count = get_union_count(counter1, counter2)

    if intersection_count == 0 and union_count == 0:
        return 65536

    return int((intersection_count / union_count) * 65536)


def split_by_2chars(s):
    ret = []
    for i in range(len(s)-1):
        ret.append(s[i] + s[i+1])
    return ret


def get_intersection_count(counter1, counter2):
    total = 0
    for word, count in counter1.items():
        if word in counter2:
            total += min(counter1[word], counter2[word])
    return total


def get_union_count(counter1, counter2):
    intersection_words = []
    for word, count in counter1.items():
        if word in counter2:
            intersection_words.append(word)

    total = 0
    for word in intersection_words:
        total += max(counter1[word], counter2[word])
        del counter1[word]
        del counter2[word]

    total += sum(list(counter1.values())) + sum(list(counter2.values()))
    return total


assert solution("FRANCE", "french") == 16384
assert solution("aa1+aa2", "AAAA12") == 43690
assert solution('handshake', 'shake hands') == 65536
assert solution("E=M*C^2", "e=m*c^2") == 65536