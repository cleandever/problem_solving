"""
https://leetcode.com/problems/single-number/
"""
from functools import reduce


class Solution:
    def dict_solution(self, nums):
        d = {}
        for n in nums:
            if n in d:
                del d[n]
            else:
                d[n] = n
        return list(d)[0]

    def xor_solution(self, nums):
        return reduce(lambda x, y: x ^ y, nums)

    def singleNumber(self, nums):
        # return self.dict_solution(nums)
        return self.xor_solution(nums)


sol = Solution()
assert sol.singleNumber([2, 2, 1]) == 1
assert sol.singleNumber([4, 1, 2, 1, 2]) == 4
