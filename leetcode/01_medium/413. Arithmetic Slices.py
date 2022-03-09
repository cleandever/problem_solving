"""
https://leetcode.com/problems/arithmetic-slices/
"""
class Solution:
    def numberOfArithmeticSlices(self, nums):
        count = 0
        total = 0
        for i in range(2, len(nums)):
            if (nums[i-2] - nums[i-1]) == (nums[i-1] - nums[i]):
                count += 1
                total += count
            else:
                count = 0
        return total


sol = Solution()
assert sol.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
assert sol.numberOfArithmeticSlices([1, 2, 3, 4, 5, 6]) == 10