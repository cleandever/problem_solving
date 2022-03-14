"""
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/submissions/
"""

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        alphabets = {c: i+1 for i, c in enumerate(alphabets)}

        num_str = ''.join([str(alphabets[c]) for c in s])
        while k > 0:
            num_str = str(sum(map(int, num_str)))
            k -= 1

        return int(num_str)


sol = Solution()

assert sol.getLucky('iiii', k=1) == 36
assert sol.getLucky('leetcode', k=2) == 6
