"""
https://programmers.co.kr/learn/courses/30/lessons/12981
"""
def solution(n, words):
    seen_words = {}
    for i, word in enumerate(words):
        person_no = (i % n) + 1
        loop_count = (i // n) + 1

        # 끝말 잇기 조건 체크
        if i > 0 and words[i-1][-1] != word[0]:
            return [person_no, loop_count]

        # 이전에 등장했던 단어 체크
        if word in seen_words:
            return [person_no, loop_count]

        seen_words[word] = 0

    return [0, 0]


assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]