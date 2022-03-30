"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
class Solution:
    def letterCombinations(self, digits):
        if not digits: return digits

        d = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        ret = []

        def recur(s, numbers):
            if not numbers:
                ret.append(s)
                return

            for c in d[int(numbers[0])]:
                recur(s + c, numbers[1:])

        recur('', digits)
        return ret
