"""
https://programmers.co.kr/learn/courses/30/lessons/12951
"""


def solution(s):
    # 공백문자가 연속해서 나올 수 있기 때문에 구분자를 명시적으로 ' '를 지정해야 함
    s = s.split(sep=' ')

    for i in range(len(s)):
        s[i] = s[i][:1].upper() + s[i][1:].lower()
    return ' '.join(s)


assert solution("3people unFollowed me") == "3people Unfollowed Me"
assert solution("for the last week") == "For The Last Week"
assert solution("a b") == "A B"
assert solution("a   b") == "A   B"
assert solution("3a  b") == "3a B"
assert solution("3a  3B") == "3a 3b"