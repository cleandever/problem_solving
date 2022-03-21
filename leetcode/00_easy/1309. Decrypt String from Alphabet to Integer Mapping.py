"""
https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        for n in range(10, 27):
            s = s.replace(f'{n}#', chr(ord('j') + (n-10)))

        for n in range(1, 10):
            s = s.replace(f'{n}', chr(ord('a') + (n-1)))

        return s


sol = Solution()
assert sol.freqAlphabets("10#11#12") == 'jkab'
assert sol.freqAlphabets("1326#") == 'acz'