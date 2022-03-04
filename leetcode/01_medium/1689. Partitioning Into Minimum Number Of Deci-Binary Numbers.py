"""
https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
"""
class Solution:
    def minPartitions(self, n):
       """
        8 2 7 3 4
        1 1 1 1 1

        7 1 6 2 3
        1 1 1 1 1

        6 0 5 1 2
        1 0 1 1 1

        5 0 4 0 1
        1 0 1 0 1

        4 0 3 0 0
        1 0 1 0 0

        3 0 2 0 0
        1 0 1 0 0

        2 0 1 0 0
        1 0 1 0 0

        1 0 0 0 0
        1 0 0 0 0
       """
       return max(list((map(int, n))))


sol = Solution()
assert sol.minPartitions('32') == 3
assert sol.minPartitions('82734') == 8
assert sol.minPartitions('27346209830709182346') == 9
