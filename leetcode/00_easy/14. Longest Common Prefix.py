"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: return ''
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        count = 0
        for c1, c2 in zip(strs[0], strs[-1]):
            if c1 != c2:
                return strs[0][:count]
            count += 1
        return strs[0][:count]

