"""
https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/
"""


class Solution:
    def executeInstructions(self, n, startPos, s):
        dirs = {
            'U': [-1, 0],
            'D': [1, 0],
            'L': [0, -1],
            'R': [0, 1],
        }

        res = []
        for i in range(len(s)):
            cur_pos = startPos.copy()
            move_cnt = 0
            for j in range(i, len(s)):
                cur_pos[0] += dirs[s[j]][0]
                cur_pos[1] += dirs[s[j]][1]

                if (0 <= cur_pos[0] < n) and (0 <= cur_pos[1] < n):
                    move_cnt += 1
                else:
                    break
            res.append(move_cnt)
        return res


sol = Solution()
assert sol.executeInstructions(3, [0, 1], "RRDDLU") == [1,5,4,3,1,0]