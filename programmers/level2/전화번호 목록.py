"""
https://programmers.co.kr/learn/courses/30/lessons/42577
"""
def solution(phone_book):
    d = {number: None for number in phone_book}

    for number in phone_book:
        prefix = ''
        for c in number:
            prefix += c

            # 자기 자신 번호 제외
            if prefix == number:
                continue

            if prefix in d:
                return False

    return True


assert solution(['1', '2', '3']) == True
assert solution(['1', '234']) == True
assert solution(['1', '123']) == False
assert solution(['234', '235']) == True
assert solution(['234']) == True
assert solution(['234', '29999', '532433']) == True
assert solution(["119", "97674223", "1195524421"]) == False
assert solution(["123","456","789"]) == True
assert solution(["12","123","1235","567","88"]) == False