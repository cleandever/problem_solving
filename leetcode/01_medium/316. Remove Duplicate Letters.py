"""
https://leetcode.com/problems/remove-duplicate-letters/
"""
from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c:
                    stack.pop()
                stack.append(c)

        return ''.join(stack)








sol = Solution()
assert sol.removeDuplicateLetters('bcabc') == 'abc'
assert sol.removeDuplicateLetters('cbacdcbc') == 'acdb'
