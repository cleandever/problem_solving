"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""
class Solution:
    def minAddToMakeValid(self, s):
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue

            if stack[-1] == '(' and c == ')':
                stack.pop()
            else:
                stack.append(c)

        return len(stack)


sol = Solution
assert sol.minAddToMakeValid("())") == 1
assert sol.minAddToMakeValid("(((") == 3