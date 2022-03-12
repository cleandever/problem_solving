"""
https://programmers.co.kr/learn/courses/30/lessons/81301
"""


numbers = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def solution1(s):
    answer = []

    num_str = ''
    for ch in s:
        if ch.isdigit():
            num_str = ''
            answer.append(ch)
        else:
            num_str += ch
            if num_str in numbers:
                answer.append(numbers[num_str])
                num_str = ''

    return int(''.join(answer))


def solution2(s):
    for k, v in numbers.items():
        s = s.replace(k, v)
    return int(s)


assert solution1('one4seveneight') == 1478
assert solution2('one4seveneight') == 1478