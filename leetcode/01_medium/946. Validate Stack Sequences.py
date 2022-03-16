"""
https://leetcode.com/problems/validate-stack-sequences/
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        stack = []
        popped_idx = 0

        while pushed:
            if stack and stack[-1] == popped[popped_idx]:
                stack.pop(-1)
                popped_idx += 1
                continue

            if pushed[0] == popped[popped_idx]:
                pushed.pop(0)
                popped_idx += 1
                continue
            stack.append(pushed[0])
            pushed.pop(0)
        return stack[::-1] == popped[popped_idx:]


sol = Solution()
assert sol.validateStackSequences([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]) == True
assert sol.validateStackSequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]) == False